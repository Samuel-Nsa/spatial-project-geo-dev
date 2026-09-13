# Week 02 Data Note: Rural Market Accessibility

**1. Marketplaces (Points of Interest)**
* **Source:** GRID3 Nigeria (Points of Interest — Markets), with 2 of 13 records attributed to eHealth Africa polio-mapping (`source` field: `GRID` vs `eHA_Polio`)
* **Geometry Type:** Point
* **Feature Count:** 13 features
* **Key Columns:** `market_nam`, `mrkt_type`, `mrkt_frqcy`, `wardname`, `mrkt_mon`–`mrkt_sun` (weekly schedule)
* **Gaps/Missing Values:** The 2 `eHA_Polio`-sourced records (Ajura, Fidiwo) have no market-frequency or weekly-schedule data, unlike the 11 `GRID`-sourced records — the two source feeds don't carry the same attributes

**2. Road Network**
* **Source:** Blended roads dataset — majority from CIESIN/Meta AI-derived roads (dated 2020), minority from Overture Maps/OSM (dated 2025), per the `source_acr` field
* **Geometry Type:** LineString / MultiLineString
* **Feature Count:** 22,488 features
* **Key Columns:** `class` (road type, e.g. residential/track/tertiary), `road_surfa`, `speed_esti`, `date`, `source_acr`
* **Gaps/Missing Values:** `road_surfa` is null for all CIESIN/Meta-sourced roads (the large majority) and only populated for the smaller Overture/OSM-sourced subset — surface quality data is structurally missing for most of the network, not just sparsely recorde

**3. Settlement Extents**
* **Source:** GRID3 Nigeria Settlements (combined dataset — `source` field shows both `GRID` and `OSGOF`, i.e. Office of the Surveyor General of the Federation, rather than a single-source download)
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
