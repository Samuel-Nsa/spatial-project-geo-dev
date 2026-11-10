import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
wards.to_file("data/processed/week10_outputs.gpkg", layer="wards")
wards.drop(columns="geometry").to_csv("month-03/week-10/wards_table.csv", index=False)
print(gpd.list_layers("data/processed/week10_outputs.gpkg"))