import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
faciilities = gpd.read_file(
    "data/processed/health_facilities.gpkg", layer="facilities"
).to_crs(epsg=32631)

wards["area_km2"] = wards.area / 1_000_000

reach = faciilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1_000_000

gaps = uncovered[["ward_name", "uncovered_km2"]]
result = wards.merge(gaps, on="ward_name", how="left")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)
print(result[["ward_name", "area_km2", "uncovered_km2", "uncovered_pct"]].round(2))