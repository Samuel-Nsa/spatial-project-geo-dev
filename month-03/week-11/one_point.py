from pyproj import Transformer

to_utm = Transformer.from_crs("EPSG:4326", "EPSG:32633", always_xy=True)
x, y = to_utm.transform(3.8964, 7.4443)
print("UTM easting:", round(x, 1), "northing:", round(y, 1))