from pathlib import Path
import rasterio
from rasterio.warp import Resampling, calculate_default_transform, reproject

target_crs = "EPSG:4326"
out_path = Path("data/processed/dem_wgs84.tif")
out_path.parent.mkdir(parents=True, exist_ok=True)

with rasterio.open("data/raw/dem.tif") as src:
    transform, width, height = calculate_default_transform(
        src.crs, target_crs, src.width, src.height, *src.bounds
    )
    profile = src.profile.copy()
    profile.update(
        crs=target_crs,
        transform=transform,
        width=width,
        height=height,
    )

    with rasterio.open(out_path, "w", **profile) as dst:
        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=target_crs,
            resampling=Resampling.bilinear,
        )

with rasterio.open(out_path) as check:
    print("New CRS:", check.crs)
    print("New pixel size:", check.res)