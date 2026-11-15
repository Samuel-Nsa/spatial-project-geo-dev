import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
print("CRS:", wards.crs)

wards["area_wrong"] = wards.area
print(wards[["ward_name", "area_wrong"]].head(3))

print("Suggested UTM:", wards.estimate_utm_crs())
wards_utm = wards.to_crs(epsg=32631)
wards_utm["area_km2"] = wards_utm.area / 1_000_000
print(wards_utm[["ward_name", "area_km2"]].head(3))
print("Ibadan North total:", round(wards_utm["area_km2"].sum(), 1), "km2")