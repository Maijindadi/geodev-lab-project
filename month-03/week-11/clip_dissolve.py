import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards"
                      ).to_crs(epsg=32631)
roads = gpd.read_file("data/processed/roads.gpkg", layer="roads"
                     ).to_crs(epsg=32631)
agodi = wards[wards["ward_name"] == "Agodi"]
agodi_roads = gpd.clip(roads, agodi)
print("roads in Agodi:", len(agodi_roads))
print("road length in agodi:", round(agodi_roads.length.sum() / 1_000, 2), "km")
lga = wards.dissolve(by="lga_name")
print(lga.reset_index()[["lga_name"]])
print("LGA Area:", round(lga.area.iloc[0] / 1_000, 1), "km")