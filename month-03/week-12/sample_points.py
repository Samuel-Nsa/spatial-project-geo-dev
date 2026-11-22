import geopandas as gpd
import rasterio

with rasterio.open("data/raw/dem.tif") as src:
    facilities = gpd.read_file(
        "data/processed/health_facilities.gpkg", layer="facilities"
    ).to_crs(src.crs)
    coords = []
    for p in facilities.geometry:
        coords.append((p.x, p.y))
    facilities["elevation_m"] = [values[0] for values in src.sample(coords)]

print(facilities[["name", "elevation_m"]].head())    