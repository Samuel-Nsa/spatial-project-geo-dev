import pandas as pd
import geopandas as gpd
table = pd.read_csv("data/raw/markets.csv")
print(table.head(3))

markets = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["X"], table["Y"]),
    crs="EPSG:32631",
)
print(markets.head(3))
print(markets.crs)

markets.to_file("data/processed/markets.gpkg", layer="markets")
print("Saved", len(markets), "markets")