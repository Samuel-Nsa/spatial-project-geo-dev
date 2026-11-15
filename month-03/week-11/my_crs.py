import geopandas as gpd
import pathlib

# Load custom spatial data
spatial_path = pathlib.Path("data/processed/obafemi_owode_settlement.gpkg")
layers = gpd.list_layers(spatial_path)['name'].tolist()
print("Available layers:", layers)

# Automatically pick the first layer in the GeoPackage
layer_name = layers[0]
gdf = gpd.read_file(spatial_path, layer=layer_name)

print("=== CRS INSPECTION ===")
print("Original CRS:", gdf.crs)
print("Estimated UTM CRS:", gdf.estimate_utm_crs())

# Ensure proper projection
if gdf.crs != "EPSG:32631":
    gdf = gdf.to_crs("EPSG:32631")

id_col = "wardname" if "wardname" in gdf.columns else gdf.columns[0]

# Use existing QGIS attribute area if present, otherwise calculate from geometry
if "area_km2" in gdf.columns and (gdf["area_km2"] > 0).any():
    print("\n=== AREA COMPUTATION (From Attribute Table) ===")
    print(gdf[[id_col, "area_km2"]].head())
    print(f"Total area: {gdf['area_km2'].sum():.2f} km²")
else:
    gdf["area_km2"] = gdf.geometry.area / 1_000_000
    print("\n=== AREA COMPUTATION (Calculated) ===")
    print(gdf[[id_col, "area_km2"]].head())
    print(f"Total calculated area: {gdf['area_km2'].sum():.2f} km²")