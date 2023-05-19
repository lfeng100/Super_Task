#!/usr/bin/env python
# coding: utf-8

# In[97]:


# Code from jupyter notebook (Python Code)

import pandas as pd
import numpy as np
import math

# Extract Data into DataFrame
data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'
data = data.split('\n')
columns = data[0].split(";")
flight_data = pd.DataFrame((row.split(";") for row in data[1:(len(data)-1)]), columns=columns)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Fill null values in FlightCodes column and convert to int
flight_data["FlightCodes"] = flight_data["FlightCodes"].replace(r'^\s*$', np.nan, regex=True).astype(float)

if len(flight_data) > 0:
    # If first FlightCode is NaN, set to arbitrary value 10000
    if math.isnan(flight_data["FlightCodes"][0]):
        flight_data["FlightCodes"][0] = 10000

    # Fill FlightCodes sequentially
    for i in range(1, len(flight_data["FlightCodes"])):
        if math.isnan(flight_data["FlightCodes"][i]): # NaN check
                flight_data.at[i, 'FlightCodes'] = flight_data["FlightCodes"][i-1] + 10

# convert to int
flight_data["FlightCodes"] = flight_data["FlightCodes"].astype(int)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. Separate To_From column to two columns and uppercase
to_column = []
from_column = []

# extract values (and uppercase them)
for i in flight_data["To_From"]:
    to_from = i.split('_')
    to_column.append(to_from[0].upper())
    from_column.append(to_from[1].upper())

# add new columns
flight_data["To"] = to_column
flight_data["From"] = from_column

# drop old column
flight_data.drop("To_From", axis=1, inplace=True)
flight_data
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3. Remove unecessary punctuation and numbers from Airline Code column
flight_data["Airline Code"] = flight_data["Airline Code"].str.replace(r'[^\w\s]|[1-9]', '', regex=True)
# strip leading/trailing whitespace
flight_data["Airline Code"] = flight_data["Airline Code"].str.strip()
print(flight_data)


# In[92]:





# In[ ]:




