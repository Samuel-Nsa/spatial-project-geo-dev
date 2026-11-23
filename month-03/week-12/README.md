# Week 12: Raster inspection, spectral indices & zonal statistics

## What this folder contains
- `my_inspect.py`: Runs the raster metadata checklist on the Obafemi-Owode SRTM 1 Arc-Second DEM tile (`data/raw/n06_e003_1arc_v3.tif`), verifying dimensions, resolution (`0.0002777777777777778°`), CRS (`EPSG:4326`), bounding box, nodata value (`-32767.0`), and affine transform, and confirming that `width * res[0]` equals `right - left` (`1.0002777777777778°`, within floating-point tolerance `4.44e-16`).
- `my_index.py`: Computes Normalized Difference Vegetation Index (`NDVI = (NIR - Red) / (NIR + Red)`) from Landsat 9 Collection 2 Level-2 surface reflectance bands (`SR_B4` and `SR_B5`) after applying the official scale factor (`0.0000275 * DN - 0.2`), masks invalid/nodata pixels (`-9999.0`), prints the valid NDVI range and mean, and saves the output raster to `data/processed/my_ndvi.tif`.
- `my_zonal.py`: Reprojects the 1,066 Obafemi-Owode settlement point locations (`data/processed/obafemi_owode_settlement.gpkg`, layer `obafemiowode_settlement_extent_`) into the NDVI raster CRS, extracts pixel-level dry-season NDVI values via `rasterio.sample`, and aggregates mean NDVI across wards.
- `my_zonal_settlement_ndvi.csv`: Sampled dry-season NDVI values across all 1,066 settlement points in Obafemi-Owode LGA.
- `my_zonal_by_ward_ndvi.csv`: Ward-level summary of settlement counts and mean dry-season NDVI grouped by `wardname`.
- `my_map.py`: Downsamples `data/processed/my_ndvi.tif` via `Resampling.average` to a memory-safe `1178x1200` preview grid and renders `my_map.png` using the `RdYlGn` colormap (`vmin=-0.2`, `vmax=0.9`) with a labeled colorbar.
- `my_map.png`: Dry-season NDVI visualization for the Obafemi-Owode LGA Landsat 9 footprint (`2026-01-28`).
- Teaching lab scripts (`inspect_raster.py`, `read_values.py`, `pixel_coords.py`, `sample_points.py`, `ndvi.py`, `plot_raster.py`, `clip_raster.py`, `zonal_stats.py`, `reproject_raster.py`, `ndvi_map.png`): Reference exercises completed on the Ibadan North dataset.

## How to run it
From the repository root using `uv`:
```bash
uv run month-03/week-12/my_inspect.py
uv run month-03/week-12/my_index.py
uv run month-03/week-12/my_zonal.py
uv run month-03/week-12/my_map.py
```

## Scene metadata & data provenance
- **Landsat Scene:** `LC09_L2SP_191055_20260128_20260129_02_T1` (Landsat 9 OLI-2/TIRS-2 Collection 2 Level-2, Path 191, Row 055)
- **Acquisition Date:** `2026-01-28` (dry season)
- **Cloud Cover:** `< 10%` land cloud cover (clear-sky scene over Obafemi-Owode LGA)
- **DEM Tile:** `SRTM1N06E003V3` (`data/raw/n06_e003_1arc_v3.tif`, SRTM 1 Arc-Second Global, `EPSG:4326`)
- **Provenance:** Raster datasets were downloaded from USGS EarthExplorer (`https://earthexplorer.usgs.gov/`) and settlement vectors from GRID3 Nigeria. Because raw `.tif` rasters and `.aux.xml` sidecars are excluded from Git via `.gitignore`, full acquisition details and file paths are documented in the root `data-notes.md`.

## What I found
- **Raster Geometry Verification:** In `n06_e003_1arc_v3.tif`, `width * res[0]` (`1.0002777777777778`) matched `right - left` (`1.0002777777777783`) with a negligible floating-point difference of `4.44e-16`, confirming exact alignment between pixel grid dimensions, resolution, and geographic bounds.
- **Urban vs. Rural Vegetation Contrast:** Zonal settlement results reveal a clear land-cover gradient across Obafemi-Owode LGA during the peak dry season. Rapidly urbanizing settlements along the Lagos–Ibadan Expressway corridor recorded the lowest mean NDVI values—including **Ibafo** (`0.2407`, 40 settlements), **Magboro** (`0.2532`, 23 settlements), and **Mowe** (`0.2829`, 70 settlements)—reflecting dense built-up surfaces and impervious cover. Conversely, interior agrarian and rural wards maintained substantially higher dry-season vegetation vigor, led by **Obafemi** (`0.5130`, 114 settlements), **Molokiki** (`0.5070`, 36 settlements), **Odeda** (`0.4958`, 2 settlements), and **Maloko Asipa** (`0.4883`, 78 settlements).

## What went wrong and how I fixed it
1. **Point vs. Polygon Geometry Mismatch in Zonal Extraction:** The Obafemi-Owode settlement dataset (`obafemi_owode_settlement.gpkg`) stores 1,066 settlement extents as `Point` geometries rather than polygon boundaries, causing polygon-based `rasterio.mask.mask()` calls to fail when searching for a `wards` polygon layer.
  - *Fix:* Adapted `my_zonal.py` to reproject the settlement points into the Landsat raster CRS (`src.crs`), extract exact pixel values using `src.sample()`, filter out `-9999.0` nodata pixels, and aggregate settlement counts and mean NDVI per ward using `groupby("wardname")`.
2. **Memory & Renderer Crashes When Plotting Full-Resolution Landsat Scenes:** Rendering the full-resolution Landsat 9 NDVI array directly in Matplotlib spiked memory usage and triggered VS Code window terminations (`reason: 'clean-exit', code: '0'`).
  - *Fix:* Switched Matplotlib to the non-interactive `Agg` backend, downsampled the raster during read (`out_shape=(1178, 1200)` with `Resampling.average`), and explicitly closed figures (`plt.close(fig)`) after saving `my_map.png`.