import geopandas as gpd
import pathlib
import matplotlib.pyplot as plt

# Load counted layer
counted_path = pathlib.Path("data/processed/obafemi_owode_market_counts.gpkg")
wards_counted = gpd.read_file(counted_path, layer="market_counts")

# Create figure
fig, ax = plt.subplots(figsize=(10, 10))
wards_counted.plot(
    column="market_count",
    cmap="YlOrRd",
    legend=True,
    legend_kwds={"label": "Market Count (5km Buffer)", "orientation": "horizontal"},
    edgecolor="black",
    linewidth=0.5,
    ax=ax
)

ax.set_title("Obafemi-Owode LGA: Market Accessibility Counts", fontsize=14, fontweight="bold")
ax.set_axis_off()

# Save PNG to the week folder
output_png = pathlib.Path("month-03/week-11/obafemi_owode_market_counts.png")
plt.savefig(output_png, dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved map PNG to {output_png}")