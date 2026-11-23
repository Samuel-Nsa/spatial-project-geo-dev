from pathlib import Path
import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio

raster_path = Path("data/processed/my_ndvi.tif")
vector_path = Path("data/processed/obafemi_owode_settlement.gpkg")
layer_name = "obafemiowode_settlement_extent_"
out_points_csv = Path("month-03/week-12/my_zonal_settlement_ndvi.csv")
out_wards_csv = Path("month-03/week-12/my_zonal_by_ward_ndvi.csv")

out_points_csv.parent.mkdir(parents=True, exist_ok=True)

with rasterio.open(raster_path) as src:
    gdf = gpd.read_file(vector_path, layer=layer_name).to_crs(src.crs)
    coords = [(geom.x, geom.y) for geom in gdf.geometry if geom is not None and not geom.is_empty]

    sampled = []
    for geom in gdf.geometry:
        if geom is None or geom.is_empty:
            sampled.append(np.nan)
            continue
        val = float(next(src.sample([(geom.x, geom.y)]))[0])
        if not np.isfinite(val) or val == -9999.0:
            sampled.append(np.nan)
        else:
            sampled.append(val)

gdf["ndvi"] = np.round(sampled, 4)

point_cols = [c for c in ["wardname", "set_name", "area_km2", "population", "ndvi"] if c in gdf.columns]
points_df = gdf[point_cols].copy()
points_df.to_csv(out_points_csv, index=False)

ward_summary = (
    points_df.dropna(subset=["ndvi"])
    .groupby("wardname", dropna=False)["ndvi"]
    .agg(settlement_count="count", mean_ndvi="mean")
    .reset_index()
)
ward_summary["mean_ndvi"] = ward_summary["mean_ndvi"].round(4)
ward_summary.to_csv(out_wards_csv, index=False)

print(f"Sampled {len(points_df)} points | Valid NDVI: {points_df['ndvi'].notna().sum()}")
print(ward_summary.head(15).to_string(index=False))
print("Saved:", out_points_csv, "and", out_wards_csv)