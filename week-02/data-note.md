# Week 02 Data Note: Rural Market Accessibility

**1. Marketplaces (Amenity Points)**
* **Source:** OpenStreetMap via Geofabrik (https://download.geofabrik.de/africa/nigeria.html)
* **Geometry Type:** Point
* **Feature Count:** [INSERT NUMBER] features
* **Key Columns:** `name`, `amenity`
* **Gaps/Missing Values:** Many smaller, informal rural markets are likely not mapped by the OSM community, which could make some areas appear more isolated than they actually are.

**2. Road Network**
* **Source:** OpenStreetMap via Geofabrik (https://download.geofabrik.de/africa/nigeria.html)
* **Geometry Type:** LineString / MultiLineString
* **Feature Count:** [INSERT NUMBER] features
* **Key Columns:** `highway`, `name`, `surface`
* **Gaps/Missing Values:** The `surface` attribute is frequently null or missing for rural feeder roads, making it difficult to determine road quality.

**3. Settlement Extents**
* **Source:** GRID3 Nigeria Settlement Extents (https://data.grid3.org/datasets/GRID3::grid3-nigeria-settlement-extents-version-01-02/about)
* **Geometry Type:** Polygon / MultiPolygon
* **Feature Count:** [INSERT NUMBER] features
* **Key Columns:** `type`, `shape_area`
* **Gaps/Missing Values:** Extremely small or newly established nomadic farming hamlets may not be captured in the satellite-derived polygons.

**4. Local Government Area Boundary**
* **Source:** Humanitarian Data Exchange - HDX (https://data.humdata.org/dataset/cod-ab-nga)
* **Geometry Type:** Polygon
* **Feature Count:** 1 feature (Obafemi Owode LGA)
* **Key Columns:** `ADM2_EN` (LGA Name), `ADM1_EN` (State Name)
* **Gaps/Missing Values:** Boundary lines are complete and clean, with no missing geometry for this specific local government area.
