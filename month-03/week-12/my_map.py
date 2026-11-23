from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.enums import Resampling

raster_path = Path("data/processed/my_ndvi.tif")
out_png = Path("month-03/week-12/my_map.png")
out_png.parent.mkdir(parents=True, exist_ok=True)

max_dim = 1200

with rasterio.open(raster_path) as src:
    scale = min(1.0, max_dim / max(src.width, src.height))
    out_h = max(1, int(round(src.height * scale)))
    out_w = max(1, int(round(src.width * scale)))

    ndvi = src.read(
        1,
        out_shape=(out_h, out_w),
        resampling=Resampling.average,
        masked=True,
    )
    ndvi = np.ma.masked_where((ndvi == -9999.0) | (~np.isfinite(ndvi)), ndvi)

fig, ax = plt.subplots(figsize=(7, 8))
image = ax.imshow(ndvi, cmap="RdYlGn", vmin=-0.2, vmax=0.9)
fig.colorbar(image, ax=ax, label="NDVI (Landsat 9, 2026-01-28)")
ax.set_title("NDVI — Obafemi-Owode LGA (Dry Season)")
ax.set_axis_off()

fig.savefig(out_png, dpi=150)
plt.close(fig)

print(f"Plotted {out_w}x{out_h} preview -> {out_png}")