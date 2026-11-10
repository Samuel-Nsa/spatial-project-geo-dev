import pandas as pd

pop = pd.read_csv("data/raw/ward_population.csv")

big = pop[pop["population_2024"] > 35000]
print(big)
print("Wards over 35,000:", len(big))

ranked = pop.sort_values("population_2024", ascending=False)
print(ranked.head(3))

pop["population_thousand"] = pop["population_2024"] / 1000
print(pop.head(3))
print("Total poulation:", pop["population_2024"].sum())