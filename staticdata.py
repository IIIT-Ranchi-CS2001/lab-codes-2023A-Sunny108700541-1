
# SET ->4  LAB EXAM PRACTICLE
import pandas as pd
import numpy as np
a=pd.read_csv("C:/Users/my lenovo/Downloads/AQI_Data.csv")
print("THIS IS TOP FIVE DATA OF DATAFRAME->")

print(a.head())    # print top 5 data
print("THIS IS LAST SIX DATA OF DATAFRAME->")
print(a.tail(6))  # print last 6 row

print("SUMMARY STATIC OF ALL NUMERIC COLUMN->")
stats = a.describe()
print(stats)

print("COMPUTE MEAN ")
print("Mean of AQI column->")
print(a['AQI'].mean())
print("Mean of PM2.5 column->")
print(a['PM2.5'].mean())
print("Mean of PM10 column->")
print(a['PM10'].mean())
#  4 QUESTION
print("Average AQI")
print(a['AQI'].mean())
print("MAXIMUM PM10")
print(a['PM10'].max())

# BY GROUPING DATA
print('GROUPED DATA->')
result = a.groupby('City').agg(
    average_AQI=('AQI', 'mean'),
    max_PM10=('PM10', 'max')
).reset_index()

# Display the result
print(result)


#a.to_csv('output.csv', sep=';', index=False, encoding='utf-8')

# Save the grouped data to a CSV file

result.to_csv('output.csv', sep=';', index=False, encoding='utf-8')

