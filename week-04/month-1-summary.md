# Month 1 Summary: Rural Market Accessibility

**The Question:** 
What proportion of rural settlements in Obafemi Owode LGA are located within a standard 5-kilometer walking or driving distance from an established marketplace?

**The Operation:** 
I ran a 5-kilometer **Buffer** operation on the `Obafemi-Owode_Markets` point layer using the EPSG:32631 (UTM Zone 31N) projected CRS to ensure distances were accurately measured in meters. Establishing this fixed Euclidean boundary was the necessary first step to define a reasonable travel threshold. Next, I **Dissolved** the overlapping buffers to create a unified accessibility zone. Finally, I used the **Count Points in Polygon** tool against the settlement layer to extract the exact numerical count of settlements falling within this service area.

**Final Answer to the Research Question:**
Using the "Count Points in Polygon" tool, I calculated that exactly **478** out of the 1,066 total rural settlements in Obafemi Owode LGA fall within a 5-kilometer Euclidean distance of an established marketplace. 

This means that only **44.8%** of the rural settlements have basic geographic access to a market, leaving a significant majority (**55.2%**) outside the standard 5km access threshold. This quantitative finding strongly aligns with the visual spatial disparity observed in the southern region of the LGA.

**Expectations vs. Results (The Four Checks):**
1. **Expectation / Row Count:** I expected the initial output buffer feature count to exactly match the input market feature count (1-to-1). The attribute table confirmed this exact match prior to dissolving.
2. **The Map Check:** Visual inspection confirmed perfectly circular buffers successfully generated around the market nodes. 
3. **Hand Verification:** Using the QGIS measure line tool, I measured from the center of "Orile-Imo Market" to its buffer edge, verifying the radius is exactly 5,000 meters.
4. **Empty Geometry:** Sorting the output attribute table confirmed there are no null or empty geometries in the results.

**What Surprised Me:** 
Looking at the map, the southern tip of the LGA contains a very dense cluster of settlement points, yet it falls entirely outside of any 5km market buffer. The spatial disparity in market access across the LGA is much wider than I anticipated.

**Data Still Needed:** 
To upgrade this from a simple Euclidean (straight-line) distance analysis to a true friction-based routing analysis, I still need accurate `road_surface` attributes (e.g., paved vs. dirt track) and detailed market operating schedules.
