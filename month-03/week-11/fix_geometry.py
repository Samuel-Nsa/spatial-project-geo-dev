from shapely.geometry import Polygon
from shapely.validation import explain_validity
import geopandas as gpd

bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
print("Valid:", bowtie.is_valid)
print("Why:", explain_validity(bowtie))

layer = gpd.GeoDataFrame({"name": ["bowtie"]}, geometry=[bowtie], crs="EPSG:32631")
layer["geometry"] = layer.make_valid()
print("Valid now:", layer.is_valid.all())
print("New type:", layer.geom_type.iloc[0])