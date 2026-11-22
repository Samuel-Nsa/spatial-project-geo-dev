# Week 02 Data Note: Rural Market Accessibility

**1. Marketplaces (Points of Interest)**
* **Source:** GRID3 Nigeria (Points of Interest — Markets) (https://data.grid3.org/datasets/grid3-nga-markets), with 2 of 13 records attributed to eHealth Africa polio-mapping (`source` field: `GRID` vs `eHA_Polio`)
* **Geometry Type:** Point
* **Feature Count:** 13 features
* **Key Columns:** `market_nam`, `mrkt_type`, `mrkt_frqcy`, `wardname`, `mrkt_mon`–`mrkt_sun` (weekly schedule)
* **Gaps/Missing Values:** The 2 `eHA_Polio`-sourced records (Ajura, Fidiwo) have no market-frequency or weekly-schedule data, unlike the 11 `GRID`-sourced records — the two source feeds don't carry the same attributes

**2. Road Network**
* **Source:** Blended roads dataset — majority from GRID3 NGA - Roads v1.0 / CIESIN AI-derived roads (https://data.grid3.org/datasets/GRID3::grid3-nga-roads/explore) (dated 2020), minority from Overture Maps (https://overturemaps.org) (dated 2025), per the `source_acr` field
* **Geometry Type:** LineString / MultiLineString
* **Feature Count:** 22,488 features
* **Key Columns:** `class` (road type, e.g. residential/track/tertiary), `road_surfa`, `speed_esti`, `date`, `source_acr`
* **Gaps/Missing Values:** `road_surfa` is null for all CIESIN/Meta-sourced roads (the large majority) and only populated for the smaller Overture/OSM-sourced subset — surface quality data is structurally missing for most of the network, not just sparsely recorde

**3. Settlement Extents**
* **Source:** GRID3 Nigeria Settlement Extents v4.0 (https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-0/about) — combined dataset; `source` field shows both `GRID` and `OSGOF` (Office of the Surveyor General of the Federation), rather than a single-source download
* **Geometry Type:** Point (confirmed via Layer Properties → Information — despite the "Extent" name, this dataset stores settlement locations as points, not polygon boundaries)
* **Feature Count:** 1,066 features
* **Key Columns:** `wardname`, `lganame`, `set_name`, `set_altnam`, `is_primary`, `source`
* **Gaps/Missing Values:** At least one record ("Ogunji") is attributed to Shagamu LGA rather than Obafemi Owode — the layer isn't fully clipped to the target LGA and needs an explicit spatial filter before use in the accessibility analysis

**4. Local Government Area Boundary**
* **Source:** Humanitarian Data Exchange - HDX (https://data.humdata.org/dataset/cod-ab-nga)
* **Geometry Type:** Polygon
* **Feature Count:** 1 feature (Obafemi Owode LGA)
* **Key Columns:** `ADM2_EN` (LGA Name), `ADM1_EN` (State Name)
* **Gaps/Missing Values:** Boundary lines are complete and clean, with no missing geometry for this specific local government area.

---

# Week 12 Data Note: Elevation & Multispectral Imagery

**5. Landsat 8-9 Collection 2 Level-2 Surface Reflectance (NDVI / Spectral Bands)**
- **Source:** USGS EarthExplorer — Landsat 8-9 OLI/TIRS C2 L2 (https://earthexplorer.usgs.gov/)
- **Scene ID:** `LC09_L2SP_191055_20260128_20260129_02_T1` (Path 191, Row 055)
- **Acquisition Date & Cloud Cover:** 2026-01-28 (Dry season; < 10% land cloud cover)
- **Geometry Type:** Raster (GeoTIFF, 30m spatial resolution)
- **Downloaded Files (kept off GitHub via `.gitignore` in `data/raw/landsat/`):**
  - `LC09_L2SP_191055_20260128_20260129_02_T1_SR_B4.TIF` (Band 4 — Red)
  - `LC09_L2SP_191055_20260128_20260129_02_T1_SR_B5.TIF` (Band 5 — Near-Infrared / NIR)
- **Notes/Limitations:** Level-2 surface reflectance values require the Collection 2 scale factor (`0.0000275 * DN - 0.2`) before computing vegetation indices such as NDVI.

**6. Digital Elevation Model (DEM)**
- **Source:** USGS EarthExplorer — SRTM 1 Arc-Second Global (https://earthexplorer.usgs.gov/)
- **Tile Entity IDs & Local Files (kept off GitHub via `.gitignore` in `data/raw/`):**
  - Primary Tile: `SRTM1N06E003V3` (`n06_e003_1arc_v3.tif` — Coordinates: 6°N, 3°E; covers primary Obafemi-Owode LGA study area)
  - Secondary Tile: `SRTM1N07E003V3` (`n07_e003_1arc_v3.tif` — Coordinates: 7°N, 3°E; northern boundary coverage)
- **Publication / Mission Date:** Published 2014-09-23 (SRTM mission captured February 2000)
- **Geometry Type & CRS:** Raster (GeoTIFF, 1 arc-second / ~30m resolution, `EPSG:4326`)
- **Notes/Limitations:** Native cells are measured in geographic degrees (`~0.00028°`); suitable for point sampling and zonal statistics after aligning vector CRS, though reprojection to a metric CRS (`EPSG:32631`) is required before calculating distance-dependent terrain metrics like slope.