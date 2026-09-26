# Rural Market Accessibility Analysis: Obafemi Owode LGA

Spatial evaluation of geographic access to formal market nodes across rural settlements in Obafemi Owode Local Government Area, Ogun State, Nigeria.

[Rural Market Accessibility Map](./week-04/Obafemi_Owode_5km_Analysis.png)

## Key Finding & Research Answer

**Research Question:** What proportion of rural settlements in Obafemi Owode LGA are located more than 5 kilometers from an established marketplace?

> **Answer:** Out of **1,066 total rural settlements** in Obafemi Owode LGA, **588 settlements (55.2%)** are located more than 5 kilometers from a recognized marketplace. Only **478 settlements (44.8%)** fall within the standard 5km accessibility buffer, revealing a significant spatial disparity in market access—particularly across the southern region of the LGA.

---

## Project Structure & Deliverables

* 📁 **[Week 1: Project Brief & Datasets](./week-01/)** — Study scope, core research questions, and source links for all spatial layers.
* 📁 **[Week 2: Data Notes & Download Metadata](./week-02/)** — Raw data inventories, attribute notes, and coordinate reference logs.
* 📁 **[Week 3: Data Preparation & Quality Checks](./week-03/data-preparation.md)** — Reprojection to EPSG:32631 (UTM Zone 31N), spatial clipping, and quality control validations.
* 📁 **[Week 4: Analysis & Integration Summary](./week-04/month-1-summary.md)** — Buffer operations, point-in-polygon calculations, map visualization, and summary documentation.

---

## Methodology Summary

1. **CRS Standardisation:** Reprojected vector layers to `EPSG:32631` (UTM Zone 31N) for distance calculations in meters.
2. **Buffer & Dissolve:** Applied a 5,000m buffer around market nodes and dissolved overlapping geometries to establish a continuous 5km service zone.
3. **Point-in-Polygon Extraction:** Ran *Count Points in Polygon* against the 1,066 settlement points to extract exact counts of accessible vs. unserved communities.

---
*Built as part of GeoDev Lab Africa (Cohort One).*
