GeoDev Lab Africa: Month 3 starter data (teaching dataset)

Copy the contents of the "data" folder into the "data" folder of your
geodev-lab-project repository, so that you have, for example:
    geodev-lab-project/data/raw/ward_population.csv
    geodev-lab-project/data/processed/wards.gpkg

What this is
The ward NAMES are real Ibadan North ward names. The ward shapes, facility
locations, population figures, roads, elevation values and Landsat band values
were generated for teaching, so that every output in the Month 3 learning pack
can be reproduced exactly. The wards are drawn as a grid of equal squares.
Do not quote any figure from this dataset as a fact about Ibadan.

Contents
data/raw/ward_population.csv        ward population table, with messy names on purpose
data/raw/health_facilities.csv      41 facilities with latitude and longitude
data/raw/lga_facilities/*.csv       one CSV per LGA for Week 13; egbeda.csv uses different headings on purpose
data/raw/dem.tif                    elevation model, EPSG:32631, 30 m, nodata -9999
data/raw/landsat/*_SR_B4.TIF, B5    Landsat 9 style red and near infrared bands, uint16, nodata 0
data/processed/wards.gpkg           layer "wards", 12 polygons, EPSG:4326
data/processed/roads.gpkg           layer "roads", 25 lines, EPSG:4326
