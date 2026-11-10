import pandas as pd
import geopandas as gpd
import pathlib

# Define file paths
spatial_path = pathlib.Path("data/processed/obafemi_owode_settlement.gpkg")
csv_path = pathlib.Path("data/raw/mydata.csv")

# 1. Load data sources
layers = gpd.list_layers(spatial_path)['name'].tolist()
gdf = gpd.read_file(spatial_path, layer=layers[0])
df = pd.read_csv(csv_path)

# 2. Print row counts BEFORE join
print("=== BEFORE JOIN ===")
print(f"Spatial layer row count: {len(gdf)}")
print(f"CSV table row count: {len(df)}")

# 3. Perform merge with explicit suffixes since both files share column names
joined = gdf.merge(df, on="wardname", suffixes=('_spatial', '_csv'), how="left")

# 4. Check match count
matched = joined["population_csv"].notna().sum()
print(f"\n=== AFTER JOIN ===")
print(f"Match count after join: {matched} of {len(gdf)}")

# 5. Preview successfully joined data
print("\nSample of joined data:")
print(joined[['wardname', 'population_csv']].head(5))