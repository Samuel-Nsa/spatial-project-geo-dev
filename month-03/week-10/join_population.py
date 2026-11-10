import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
pop = pd.read_csv("data/raw/ward_population.csv")

first_try = wards.merge(pop, left_on="ward_name", right_on="ward", how="left")
matched = first_try["population_2024"].notna().sum()
print("Matched on first try:", matched, "of", len(wards))

def clean_name(name):
    return name.strip().upper().replace("-", "")
wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("Matched on second try:", matched, "of", len(wards))
print(joined[["ward_name", "ward", "population_2024"]])