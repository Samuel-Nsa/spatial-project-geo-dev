import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

target_crs = "EPSG:4326"

with rasterio.open("data/raw/dem.tif") as src:
    transform, width, height = calculate_default_transform(
        src.crs, target_crs, src.width, src.height, *src.bounds
    )
    profile = src.profile
    profile.update(crs=target_crs, transform=transform, width=width, height=height)

    with rasterio.open("data/processed/dem_wgs84.tif", "w", **profile) as dst:
        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=target_crs,
            resampling=Resampling.bilinear,
        )

with rasterio.open("data/processed/dem_wgs84.tif") as check:
    print("New CRS:", check.crs)
    print("New pixel size:", check.res)