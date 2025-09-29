import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/globalpowerplantdatabasev130/interim/global_power_plant_database_preprocessed.csv")

# Log scaling of generation_gwh_{year}
"""
Filtering out generation_gwh_{year} < 0 
This removes a unrealistc rows from the dataset becuase log return s0 when a value is between 0 and 1. The smallest plant in this data set is 1 MW,
so a <1 gwh generation rate is very unlikely.
"""
df["log_capacity_mw"] = np.log1p(df["capacity_mw"])
df["log_generation_gwh_2013"] = np.log1p(df["generation_gwh_2013"])
df["log_generation_gwh_2014"] = np.log1p(df["generation_gwh_2014"])
df["log_generation_gwh_2015"] = np.log1p(df["generation_gwh_2015"])
df["log_generation_gwh_2016"] = np.log1p(df["generation_gwh_2016"])
df["log_generation_gwh_2017"] = np.log1p(df["generation_gwh_2017"])
df["log_generation_gwh_2018"] = np.log1p(df["generation_gwh_2018"])
df["log_generation_gwh_2019"] = np.log1p(df["generation_gwh_2019"])

# Compute avg_generation_gwh
df["avg_generation_gwh"] = df[[f"generation_gwh_{y}" for y in range(2013, 2020)]].mean(axis=1)

# Log scaling to make data more graphically meaningful
df["log_avg_generation_gwh"] = np.log1p(df["avg_generation_gwh"])

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