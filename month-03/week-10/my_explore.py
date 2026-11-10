import geopandas as gpd

file_path = "data/raw/obafemi_owode_layers.gpkg"

print("Layers available:", gpd.list_layers(file_path))

# Read the file without specifying a layer name to load the default layer
gdf = gpd.read_file(file_path)

print(gdf.head())
print("Rows and columns:", gdf.shape)
print(gdf.geom_type.value_counts())
print("CRS:", gdf.crs)
print("Bounds:", gdf.total_bounds)