import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
first = wards.geometry.iloc[0].exterior.coords[0]
print("Original first corner:", first)

projected = wards.to_crs(epsg=32631)
print("After to_crs:", projected.geometry.iloc[0].exterior.coords[0])

wrongly_labelled = wards.set_crs(epsg=32631, allow_override=True)
print("After set_crs:", wrongly_labelled.geometry.iloc[0].exterior.coords[0])
print("Label now says:", wrongly_labelled.crs)