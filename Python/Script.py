"""

@author: david
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

planes = pd.read_csv(r'C:\Users\david\Downloads\planes_original_structure_usd_routes_scaled_prices.csv',
                     parse_dates=['Date_of_Journey'])

#Extract hours and minutes and possibly days
planes['duration_float'] = (
    planes['Duration']
    .str.extract(r'(?:(\d+)d)?\s*(?:(\d+)h)?\s*(?:(\d+)m)?')  # groups: days, hours, minutes
    .astype(float)
    .fillna(0)    # replace NaN with 0
    .pipe(lambda df: df[0]*24 + df[1] + df[2]/60)  # convert days→hours, add hours + minutes
)


#Changing the data type of total stops to create the heatmap
print()
print(planes['Total_Stops'])
planes['Total_Stops'] = planes['Total_Stops'].str.replace(" stops", "")
planes['Total_Stops'] = planes['Total_Stops'].str.replace(" stop", "")
planes['Total_Stops'] = planes['Total_Stops'].str.replace("non-stop", "0")
planes['Total_Stops'] = planes['Total_Stops'].astype(float)
print(planes['Total_Stops'].value_counts())

#Heatmap of numeric variables only
plt.figure(1)
sns.heatmap(planes.corr(numeric_only=True),annot=True)

#Transforming date of Journey
planes['Date_of_Journey']=pd.to_datetime(planes['Date_of_Journey'],dayfirst=True)

#Getting new fields
planes['month']=planes['Date_of_Journey'].dt.month
planes['weekday']=planes['Date_of_Journey'].dt.weekday

#Transforming dep times and arrival times to time format
planes['Dep_Time'] = pd.to_datetime(planes['Dep_Time'], errors="coerce", infer_datetime_format=True)
planes['Arrival_Time'] = pd.to_datetime(planes['Arrival_Time'], errors="coerce", infer_datetime_format=True)

planes['Dep_Hour'] = planes['Dep_Time'].dt.hour
planes['Arrival_Hour'] = planes['Arrival_Time'].dt.hour

#Renaming key columns (price and duration)
planes.rename(columns = {'Price':'Price_USD','duration_float':'Duration_in_Hours'},inplace = True)
print(planes.dtypes)

#Heatmap of numeric variables only with new created columns
plt.figure(2)
sns.heatmap(planes.corr(numeric_only=True),annot=True)

#Scatter plot by airline and price/duration
plt.figure(3)
sns.relplot(data= planes,
            x = 'Duration_in_Hours',
            y = 'Price_USD',
            col = 'Airline',
            kind = 'scatter',
            hue = 'Total_Stops',
            col_wrap = 2
            )

plt.show()
