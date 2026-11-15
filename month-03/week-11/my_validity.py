import geopandas as gpd
import pathlib
from shapely.validation import make_valid

# 1. Load Obafemi-Owode polygon layer
spatial_path = pathlib.Path("data/processed/obafemi_owode_settlement.gpkg")
layers = gpd.list_layers(spatial_path)['name'].tolist()
print("Available layers in GeoPackage:", layers)

target_layer = layers[0]
for lname in layers:
    test_gdf = gpd.read_file(spatial_path, layer=lname)
    if not test_gdf.empty and test_gdf.geom_type.isin(["Polygon", "MultiPolygon"]).any():
        target_layer = lname
        break

print(f"Using polygon layer: '{target_layer}'")
wards = gpd.read_file(spatial_path, layer=target_layer)

print("\n=== GEOMETRY VALIDITY CHECK ===")

# 2. Count invalid geometries BEFORE fix
invalid_before = (~wards.geometry.is_valid).sum()
print(f"Invalid geometries BEFORE fix: {invalid_before}")

# 3. Fix invalid geometries using make_valid
wards["geometry"] = wards["geometry"].apply(lambda geom: make_valid(geom) if not geom.is_valid else geom)

# 4. Count invalid geometries AFTER fix
invalid_after = (~wards.geometry.is_valid).sum()
print(f"Invalid geometries AFTER fix: {invalid_after}")

if invalid_before == 0:
    print("All polygon geometries were already valid.")
else:
    print(f"Successfully repaired {invalid_before} invalid geometry/geometries.")