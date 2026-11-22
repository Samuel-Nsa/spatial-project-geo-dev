import matplotlib.pyplot as plt
import rasterio

with rasterio.open("data/processed/ndvi.tif") as src:
    ndvi = src.read(1, masked=True)
fig, ax = plt.subplots(figsize=(7, 8))
image = ax.imshow(ndvi, cmap="RdYlGn", vmin=-0.2, vmax=0.9)
fig.colorbar(image, ax=ax, label="NDVI")
ax.set_title("Vegetation index, Ibadan North")
ax.set_axis_off()
fig.savefig("month-03/week-12/ndvi_map.png", dpi=150, bbox_inches="tight")
print("Saved ndvi_map.png")