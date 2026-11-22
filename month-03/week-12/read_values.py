import rasterio
import numpy as np

with rasterio.open("data/raw/dem.tif") as src:
    elevation = src.read(1)
    print("Array shape:", elevation.shape)
    print("Smallest value:", elevation.min())

    elevation = src.read(1, masked=True)
    print("Smallest real value:", round(float(elevation.min()), 1))
    print("Largest real value:", round(float(elevation.max()), 1))
    print("Mean real value:", round(float(elevation.mean()), 1))
    print("Nodata cells:", int((elevation.mask.sum())))