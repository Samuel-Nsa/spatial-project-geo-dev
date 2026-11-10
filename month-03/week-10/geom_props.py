import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
first = wards.geometry.iloc[0]
print(type(first))
print(first)
print("Valid:", first.is_valid)
print("Centroid:", first.centroid)