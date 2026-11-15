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

print("\n=== NEAREST MARKET REACH ANALYSIS ===")

# 3. Compute ward centroids for distance measurement
wards["centroid"] = wards.geometry.centroid
wards_centroids = wards.set_geometry("centroid")

# 4. Find nearest market using sjoin_nearest
nearest = gpd.sjoin_nearest(
    wards_centroids[[id_col, "centroid"]], 
    markets_gdf[["geometry"]], 
    how="left", 
    distance_col="distance_meters"
)

nearest["distance_km"] = nearest["distance_meters"] / 1000

print(nearest[[id_col, "distance_km"]].head(12))
print(f"Average distance to nearest market: {nearest['distance_km'].mean():.2f} km")

# 5. Save output layer to GeoPackage
output_path = pathlib.Path("data/processed/obafemi_owode_nearest_market.gpkg")
nearest.to_file(output_path, layer="nearest_market", driver="GPKG")
print(f"Saved nearest market layer to {output_path}")