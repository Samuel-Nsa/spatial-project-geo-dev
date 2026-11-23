from pathlib import Path
import numpy as np
import rasterio

folder = "data/raw/landsat/"
scene = "LC09_L2SP_191055_20260128_20260129_02_T1"
out_path = Path("data/processed/my_ndvi.tif")
out_path.parent.mkdir(parents=True, exist_ok=True)

with rasterio.open(f"{folder}{scene}_SR_B4.TIF") as red_src:
    red_raw = red_src.read(1).astype("float32")
    profile = red_src.profile

with rasterio.open(f"{folder}{scene}_SR_B5.TIF") as nir_src:
    nir_raw = nir_src.read(1).astype("float32")

valid = (red_raw > 0) & (nir_raw > 0)

red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

ndvi = np.full(red.shape, -9999.0, dtype="float32")
denom = nir + red
ok = valid & (denom != 0)

ndvi[ok] = (nir[ok] - red[ok]) / denom[ok]

low = round(float(ndvi[ok].min()), 3)
high = round(float(ndvi[ok].max()), 3)
mean_val = round(float(ndvi[ok].mean()), 3)

print("NDVI range:", low, "to", high)
print("Mean NDVI:", mean_val)

profile.update(dtype="float32", nodata=-9999.0, count=1, compress="lzw")
with rasterio.open(out_path, "w", **profile) as dst:
    dst.write(ndvi, 1)

print("Saved", out_path)