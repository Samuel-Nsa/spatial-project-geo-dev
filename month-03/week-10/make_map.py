import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
facilities = gpd.read_file("data/processed/health_facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Health facilities in Ibadan North")
ax.set_axis_off()

fig.savefig("month-03/week-10/facilities_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
