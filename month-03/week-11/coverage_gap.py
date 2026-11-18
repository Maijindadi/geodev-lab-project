import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards"
                      ).to_crs(epsg=32631)
facilities = gpd.read_file("data/processed/facilities.gpkg", layer="facilities"
                          ).to_crs(epsg=32631)
wards["area_km2"] = wards.area / 1_000_000
reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1_000_000

gaps = uncovered[["ward_name", "uncovered_km2"]]
results = wards.merge(gaps, on="ward_name", how="left")
results["uncovered_km2"] = results["uncovered_km2"].fillna(0)
share =  results["uncovered_km2"] / results["area_km2"] * 100
results["coverage_percent"] = share.round(1)
print(results[["ward_name", "area_km2", "uncovered_km2", "coverage_percent"]].round(2))
