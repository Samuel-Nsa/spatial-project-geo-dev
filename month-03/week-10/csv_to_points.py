import pandas as pd
import geopandas as gpd
table = pd.read_csv("data/raw/health_facilities.csv")
print(table.head(3))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)
print(facilities.head(3))
print(facilities.crs)

facilities.to_file("data/processed/health_facilities.gpkg", layer="facilities")
print("Saved", len(facilities), "facilities")
