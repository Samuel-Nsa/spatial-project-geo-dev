## Week 03 Data Note: Rural Market Accessibility (Data Preparation)

### 1. CRS and Preparation Workflow
- **Original State:** All source layers (Marketplaces, Road Network, Settlement Extents, and LGA Boundary) were provided in EPSG:4326 (WGS 84).
- **Study Area & Clipping:** Layers were spatially clipped to the Obafemi Owode LGA boundary polygon to remove out-of-bounds data.
- **Reprojection:** All clipped layers were reprojected to **EPSG:32631 (WGS 84 / UTM zone 31N)**. 
- **Justification:** Obafemi Owode, Ogun State is located in western Nigeria, which falls within UTM Zone 31N. A projected coordinate system measured in meters is necessary to accurately compute the 5-kilometer Euclidean service areas around the market nodes.
- **Output:** The analysis-ready layers are consolidated into a single GeoPackage (`study_area.gpkg`) stored in the `data/processed/` directory. Raw files remain untouched in `data/raw/`.

### 2. Quality Checks
- **COMPLETENESS:** High. The clipped dataset yields dense coverage, retaining 1,066 settlement points and a robust road network originally counting 22,488 features. 
- **CURRENCY:** Good. The road network includes highly recent Overture Maps/OSM data (dated 2025), capturing newly mapped rural tracks. 
- **POSITIONAL:** Adequate. Settlement nodes (captured as points) and market points align consistently, allowing for reliable distance measurements. 
- **ATTRIBUTE:** Poor but acceptable. The `road_surface` attribute is null for the majority of the CIESIN/GRID3-sourced roads, and market frequency schedules are missing for e-HA sourced points. 
- **FITNESS:** Fit for purpose. While missing road surface attributes prevent a friction-based routing analysis, the spatial geometries are fully adequate for generating the 5-kilometer buffers required to evaluate basic rural accessibility.

### 3. Problems Found and Fixed
- **Issue:** The raw settlement and road network datasets contained features extending beyond the target study area, including outlier settlements belonging to neighboring LGAs (e.g., Shagamu).
- **Resolution:** I applied a strict spatial clip using the Obafemi Owode LGA boundary prior to reprojection. This eliminated the geographical overreach and ensured the final GeoPackage only contains data relevant to the specific study area.
- **Geographical Overreach:** The raw settlement datasets contained features extending beyond the target study area, including outliers in neighboring LGAs (e.g., Shagamu). This was resolved by applying a strict spatial clip using the Obafemi Owode boundary.
- **CRS Projection Error:** Initially, a layer was incorrectly assigned to EPSG:32632 (UTM Zone 32N). Because Ogun State sits between 3° and 4° East, it actually belongs in Zone 31N. The incorrect 32N assignment corrupted the geometry extents. I discarded the corrupted file and properly reprojected the raw WGS 84 layer to **EPSG:32631 (UTM Zone 31N)**, which resolved the negative extent errors.
