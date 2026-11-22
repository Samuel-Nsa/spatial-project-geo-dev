import geopandas as gpd
import rasterio
from rasterio.mask import mask

with rasterio.open("data/raw/dem.tif") as src:
    wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(src.crs)
    study_area = wards.dissolve()
    clipped, clipped_transform = mask(src, study_area.geometry, crop=True)
    profile = src.profile
    print("Before clip:", src.width, "x", src.height, "pixels")

profile.update(
    height=clipped.shape[1], width=clipped.shape[1], transform=clipped_transform 
)
with rasterio.open("data/processed/dem_ibadan_north.tif", "w", **profile) as dst:
    dst.write(clipped)

print("After clip:", clipped.shape[2], "x", clipped.shape[1], "pixels")        