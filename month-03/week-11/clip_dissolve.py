import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
roads = gpd.read_file("data/processed/roads.gpkg", layer="roads").to_crs(epsg=32631)

agodi = wards[wards["ward_name"] == "Agodi"]
agodi_roads = gpd.clip(roads, agodi)
print("Roads in Agodi:", len(agodi_roads))
print("Road length in Agodi:", round(agodi_roads.length.sum()/ 1000, 2), "km")
lga = wards.dissolve(by="lga_name")
print(lga.reset_index()[["lga_name"]])
print("LGA area:", round(lga.area.iloc[0] / 1_000_000, 1), "km2")