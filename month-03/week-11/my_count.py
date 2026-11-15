import geopandas as gpd
import pandas as pd
import pathlib
from shapely.validation import make_valid

# 1. Load Obafemi-Owode polygon layer
spatial_path = pathlib.Path("data/processed/obafemi_owode_settlement.gpkg")
layers = gpd.list_layers(spatial_path)['name'].tolist()
print("Available layers in GeoPackage:", layers)

# Automatically select the polygon layer
target_layer = layers[0]
for lname in layers:
    test_gdf = gpd.read_file(spatial_path, layer=lname)
    if not test_gdf.empty and test_gdf.geom_type.isin(["Polygon", "MultiPolygon"]).any():
        target_layer = lname
        break

print(f"Using polygon layer: '{target_layer}'")
wards = gpd.read_file(spatial_path, layer=target_layer)

# Ensure CRS is EPSG:32631 (UTM Zone 31N)
if wards.crs is None:
    wards = wards.set_crs("EPSG:32631")
elif str(wards.crs) != "EPSG:32631":
    wards = wards.to_crs("EPSG:32631")

# Fix invalid polygon geometries
wards["geometry"] = wards["geometry"].apply(lambda geom: make_valid(geom) if not geom.is_valid else geom)

print(f"Wards CRS: {wards.crs}")
print(f"Wards bounds: {wards.total_bounds}")

# Identify the correct grouping/ward name column
id_col = "wardname" if "wardname" in wards.columns else (wards.columns[0] if len(wards.columns) > 0 else "id")
print(f"Using grouping column: '{id_col}'")

# 2. Load markets CSV and create GeoDataFrame
markets_df = pd.read_csv("data/raw/markets.csv")
print(f"Loaded {len(markets_df)} raw markets from CSV.")

x_col = "X" if "X" in markets_df.columns else "longitude"
y_col = "Y" if "Y" in markets_df.columns else "latitude"

markets_gdf = gpd.GeoDataFrame(
    markets_df,
    geometry=gpd.points_from_xy(markets_df[x_col], markets_df[y_col]),
    crs="EPSG:32631"
)

# 3. Apply 5,000-meter buffer around markets
print("Applying 5,000m buffer to markets...")
markets_buffered = markets_gdf.copy()
markets_buffered["geometry"] = markets_gdf.buffer(5000)

print("\n=== BUFFERED POINT-IN-POLYGON COUNT ===")

# 4. Spatial join using 'intersects' between buffered markets and wards
joined = gpd.sjoin(
    markets_buffered[["geometry"]], 
    wards[[id_col, "geometry"]], 
    how="inner", 
    predicate="intersects"
)
print(f"Successfully joined geometries: {len(joined)}")

# 5. Group by ward/settlement identifier and count points
counts = joined.groupby(id_col).size().rename("market_count").reset_index()

# 6. Merge back so every polygon has a count, filling unserved polygons with 0
wards_counted = wards.merge(counts, on=id_col, how="left")
wards_counted["market_count"] = wards_counted["market_count"].fillna(0).astype(int)

print(wards_counted[[id_col, "market_count"]].head(12))
print(f"Total counted intersections: {wards_counted['market_count'].sum()}")

# 7. Save processed counted layer to GeoPackage
output_path = pathlib.Path("data/processed/obafemi_owode_market_counts.gpkg")
wards_counted.to_file(output_path, layer="market_counts", driver="GPKG")
print(f"Saved counted layer to {output_path}")