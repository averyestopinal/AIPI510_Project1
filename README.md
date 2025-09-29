# AIPI510_Project1

# Overview:
This project studies the Global Power Plant Database on grounds of primary fuel type to anyalze the genration rate, capacity, runtime, and capacity factor. This data is usedful for anaylsis of energy grid modernization, fuel type choice, and power plant density.

# Citation: 
Global Energy Observatory, Google, KTH Royal Institute of Technology in Stockholm, Enipedia, World Resources Institute. 2019. Global Power Plant Database. Published on Resource Watch and Google Earth Engine. http://resourcewatch.org/ https://earthengine.google.com/  

Dataset Description:
This dataset provides information on power generation plants from around the world. The dataset is not complete, but this is expected due to [privacy of private companies and sensitive government information. The data is recorded up to 2019. There are 34936 rows of data provided amd columns include: 

country, country_long, name, gppd_idnr, capacity_mw, latitude, longitude, primary_fuel, other_fuel1, other_fuel2, other_fuel3, commissioning_year, owner, source, url, geolocation_source, wepp_id, year_of_capacity_data, generation_gwh_2013, generation_gwh_2014, generation_gwh_2015, generation_gwh_2016, generation_gwh_2017, generation_gwh_2018, generation_gwh_2019, generation_data_source, estimated_generation_gwh_2013, estimated_generation_gwh_2014, estimated_generation_gwh_2015, estimated_generation_gwh_2016, estimated_generation_gwh_2017, estimated_generation_note_2013, estimated_generation_note_2014, estimated_generation_note_2015, estimated_generation_note_2016, estimated_generation_note_2017

Estimations are provided by an method given here: https://www.wri.org/publication/estimating-power-plant-generation-global-power-plant-database


# Analysis:

git clone https://github.com/averyestopinal/AIPI510_Project1.git
cd AIPI510_Project1

Getting Data 
    Download Data Here: https://datasets.wri.org/dataset/globalpowerplantdatabase
    Version 1.3.0
    Place the files in `data/raw/`

pip install -r requirements.txt

python scripts/preprocessing.py
Look here for EDA: notebooks/exploratory_data_analysis.ipynb
python scripts/feature_engineering.py

Cleaned data in data/cleaned/
