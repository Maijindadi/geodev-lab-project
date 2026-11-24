import rasterio

with rasterio.open("data/raw/dem.tif") as src:
    print("Width x Height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data types:", src.dtypes)
    print("CRS:", src.crs)
    print("Bounds:", src.bounds)
    print("Pixel size:", src.res)
    print("No data:", src.nodata)
    print("Transform:")
    print(src.transform)
    