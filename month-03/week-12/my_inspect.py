import rasterio

raster_path = "data/raw/n06_e003_1arc_v3.tif"

with rasterio.open(raster_path) as src:
    print("File:", raster_path)
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("Nodata:", src.nodata)
    print("Transform:")
    print(src.transform)

    calc_width_span = src.width * src.res[0]
    bounds_width_span = src.bounds.right - src.bounds.left
    diff = abs(calc_width_span - bounds_width_span)

    print("Width * res[0]:", calc_width_span)
    print("Right - left:", bounds_width_span)
    print("Difference:", diff)
    print("Matches within tolerance (1e-6):", diff < 1e-6)