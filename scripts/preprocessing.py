import pandas as pd
import matplotlib
import sklearn

# Loading dataset to dataframe
df = pd.read_csv("data/globalpowerplantdatabasev130/raw/global_power_plant_database.csv")

# Checking what primary_fuel contains
print(df['primary_fuel'].unique())

# Data Structure
print("Data Structure")
print("---------------")
print(f"Dimensions: {df.shape}")
print(f"Data Types:\n{df.dtypes}")
print(f"Missing Values:\n{df.isnull().sum()}")

"""
There is a large amount of missing data for other_fuel1, other_fuel2, and other_fuel3,
but this should be expected due to some palnts only having one fuel type. Therefore,
empty values here should be filled with "None" instead of NULL.
"""

# Filling empty entries for other_fuel1, other_fuel2, and other_fuel3 with "None"
df["other_fuel1"] = df["other_fuel1"].fillna("None")
df["other_fuel2"] = df["other_fuel2"].fillna("None")
df["other_fuel3"] = df["other_fuel3"].fillna("None")

"""
For generation_gwh_2013, generation_gwh_2014, generation_gwh_2015, generation_gwh_2016, and generation_gwh_2017,
if there is a null value it should be filled with the corresponding estimated_generation_{year} if estimated_generation_{year}
is not null
"""

# Filling missing gerenation_gwh with estimate
for y in {2013, 2014, 2015, 2016, 2017}:
    gen_col = f"generation_gwh_{y}"
    est_col = f"estimated_generation_gwh_{y}"
    df[gen_col] = df[gen_col].fillna(df[est_col])

"""
Estimation has already been used to fill in null values, so it is dropped now because it no longer provides 
any value to the data
"""

# If generation_gwh_year is still missing, fill with mean
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
gen_cols = [f"generation_gwh_{y}" for y in years]
row_means = df[gen_cols].mean(axis=1, skipna=True)
for col in gen_cols:
    df[col] = df[col].fillna(row_means)

# Throw out 1512 rows that have no generation_gwh data
df.dropna(subset=["estimated_generation_gwh_2013", "estimated_generation_gwh_2014", "estimated_generation_gwh_2015", "estimated_generation_gwh_2016", "estimated_generation_gwh_2017"], how="all", inplace=True)

# Drop estimation columns amd estimation column notes
df.drop(columns=["estimated_generation_gwh_2013", "estimated_generation_gwh_2014", "estimated_generation_gwh_2015", "estimated_generation_gwh_2016", "estimated_generation_gwh_2017"], inplace=True)
df.drop(columns=["estimated_generation_note_2013", "estimated_generation_note_2014", "estimated_generation_note_2015", "estimated_generation_note_2016", "estimated_generation_note_2017"], inplace=True)

# Drop columns: source, url, geolocation_source, generation_data_source
df.drop(columns =["source", "url", "geolocation_source", "generation_data_source"] , inplace=True)

"""
There is no meaningful way to fill commissioning_year, owner, wepp_id, year_of_capacity_data
This is because these are distinct attributes to each power plant
These columns are not useless though; for example, avg generation_mwh vs commissioning_year is useful to studying efficiency increases
"""

# Data structure after preprocessing
print("Data Structure After Preprocessing")
print("---------------")
print(f"Dimensions: {df.shape}")
print(f"Data Types:\n{df.dtypes}")
print(f"Missing Values:\n{df.isnull().sum()}")

"""
The only remaining missing values are in columns that are not estimatable
To not lose a significant number of rows, these nulls are kept
"""

# Save preprocessed data to data/interim
df.to_csv("data/globalpowerplantdatabasev130/interim/global_power_plant_database_preprocessed.csv", index=False)