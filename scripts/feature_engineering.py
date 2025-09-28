import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/globalpowerplantdatabasev130/interim/global_power_plant_database_preprocessed.csv")

# Compute avg_generation_gwh
df["avg_generation_gwh"] = df[[f"generation_gwh_{y}" for y in range(2013, 2020)]].mean(axis=1)

# Compute runtime hours
df["runtime"] = (df["avg_generation_gwh"] * 1000) / df["capacity_mw"]

# Cap runtime at the number of hours in a year because >8760 hours is not possible
df["runtime"] = df["runtime"].clip(upper=8760)

# Also compute capacity factor (0–1 scale, easier to interpret)
df["capacity_factor"] = df["runtime"] / 8760

# Filter out capacity factor > 0, because this is not possible, and therefore these data points are not valid
df = df[(df["capacity_factor"] >= 0) & (df["capacity_factor"] <= 1)]
df = df[df["runtime"] >= 365]

# Save df to csv in cleaned/
df.to_csv("data/globalpowerplantdatabasev130/cleaned/global_power_plant_database_cleaned.csv", index=False)