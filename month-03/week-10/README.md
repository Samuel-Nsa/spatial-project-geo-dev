# Week 10: GeoPandas, layers as tables & spatial joins

## What this folder contains
- `my_explore.py`: Inspects schema, coordinate reference systems (EPSG:32631), and layer structures of the Obafemi-Owode GeoPackage.
- `my_points.py`: Processes and saves point vector layers (markets) for spatial analysis and coordinate verification.
- `my_join.py`: Merges demographic data (`mydata.csv`, 1,066 rows) with custom settlement/ward polygon layers, verifying pre- and post-join match counts.
- `my_map.py`: Generates and saves the population density distribution map (`population_map.png`).
- `population_map.png`: Final visualization of the custom settlement layers colored by population using the `Greens` colormap.

## How to run it
From the repository root using `uv`:
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
uv run month-03/week-10/my_map.py

## What I found
- Successfully loaded and validated 1,066 demographic records from `mydata.csv` alongside custom multi-row spatial features from `obafemi_owode_settlement.gpkg`.
- Verified that all datasets are properly projected in UTM Zone 31N (`EPSG:32631`).
- Executed the join and successfully rendered a population distribution choropleth map, saved as `population_map.png` using the `Greens` colormap.

## What went wrong and how I fixed it
1. **Single vs. Multi-Row Layer Scope:** Initially, loading the default raw vector layer returned a single LGA boundary polygon rather than the individual settlement/ward rows needed to match `mydata.csv`.
   - *Fix:* Exported and structured the multi-row settlement polygon layer from QGIS, saving it as `obafemi_owode_settlement.gpkg` in the `data/processed/` directory.
2. **Column Name Collisions During Merge:** Merging the spatial dataframe and CSV table directly caused attribute conflicts and indexing errors because both files shared identical column names (`wardname`, `population`, `area_km2`).
   - *Fix:* Added explicit column suffixes (`_spatial`, `_csv`) during the `df.merge()` operation to successfully verify match counts without naming collisions.