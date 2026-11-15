# Week 11: CRS checks, spatial operations & proximity analysis

## What this folder contains
- `my_crs.py`: Inspects layer coordinate reference systems, estimates the appropriate UTM zone (`EPSG:32631`), reprojects spatial datasets, and computes settlement polygon areas in square kilometers (km²).
- `my_count.py`: Applies a 5,000-meter buffer around market points and executes a point-in-polygon spatial join (`sjoin`) to count market accessibility per settlement/ward, retaining zero counts.
- `my_reach.py`: Calculates the nearest market travel distance from settlement ward centroids using `sjoin_nearest` and converts measurements from meters to kilometers.
- `my_validity.py`: Inspects settlement polygon geometries for validity, counts any invalid rings before and after, and repairs them using `make_valid()`.
- `my_map.py`: Generates and saves the market accessibility distribution map (`obafemi_owode_market_counts.png`).
- `obafemi_owode_market_counts.png`: Final visualization of Obafemi-Owode settlement polygons colored by 5km buffered market counts using the `YlOrRd` colormap.

## How to run it
From the repository root using `uv`:
uv run month-03/week-11/my_crs.py
uv run month-03/week-11/my_count.py
uv run month-03/week-11/my_reach.py
uv run month-03/week-11/my_validity.py
uv run month-03/week-11/my_map.py

## What I found
- Successfully validated and projected all spatial layers to UTM Zone 31N (`EPSG:32631`), enabling precise metric area calculations and spatial distance measurements.
- Executed 5,000m buffered spatial joins and nearest market proximity analyses across all Obafemi-Owode settlement polygons.
- Verified polygon topology, confirming clean geometry validity across the dataset, and rendered a market accessibility choropleth map saved as `obafemi_owode_market_counts.png`.

## What went wrong and how I fixed it
1. **Spatial Join Intersections Returning Zero Counts:** Initially, raw point-in-polygon joins returned zero intersections because market points and settlement layers required strict metric coordinate alignment and operational buffering.
   - *Fix:* Enforced explicit reprojection to `EPSG:32631`, applied a 5,000-meter buffer (`markets_gdf.buffer(5000)`) around market points, and verified bounds before executing `gpd.sjoin()`.
2. **Polygon Topology & Geometry Verification:** Ensuring that spatial indexes and polygon boundaries were fully robust against potential self-intersections or invalid rings.
   - *Fix:* Integrated `make_valid` from `shapely.validation` across the polygon processing pipeline to guarantee clean geometric intersections and reliable spatial operations.