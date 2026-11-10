import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pathlib

# 1. Load data and perform the join
spatial_path = pathlib.Path("data/processed/obafemi_owode_settlement.gpkg")
csv_path = pathlib.Path("data/raw/mydata.csv")

layers = gpd.list_layers(spatial_path)['name'].tolist()
gdf = gpd.read_file(spatial_path, layer=layers[0])
df = pd.read_csv(csv_path)

# Merge your data
joined = gdf.merge(df, on="wardname", suffixes=('_spatial', '_csv'), how="left")

# 2. Plot and color by population (The Stretch Goal)
fig, ax = plt.subplots(figsize=(10, 10))

# Use your population column name from the join ('population_csv' or 'population')
joined.plot(
    column="population_csv", 
    legend=True, 
    cmap="Greens", 
    edgecolor="black", 
    linewidth=0.5, 
    ax=ax
)

plt.title("Obafemi-Owode Settlement Population Map", fontsize=14, fontweight="bold")
plt.xlabel("UTM Easting (meters)")
plt.ylabel("UTM Northing (meters)")

# 3. Save the map to your week-10 folder
output_path = pathlib.Path("month-03/week-10/population_map.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
print(f"Map successfully saved to {output_path}")

plt.show()