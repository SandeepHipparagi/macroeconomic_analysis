#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Step 1: Data Collection

import requests
import csv

data_source_url = "https://example.com/macroeconomic_data"
output_csv_file = "macroeconomic_data.csv"

response = requests.get(data_source_url)
data = response.json()

with open(output_csv_file, "w", newline="") as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


# In[ ]:


#Step 2: Step Processing

import pandas as pd

input_csv_file = "macroeconomic_data.csv"
output_processed_csv = "processed_macroeconomic_data.csv"

data = pd.read_csv(input_csv_file)

# Calculate average GDP and inflation rate
data["Average_GDP"] = data[["GDP_Q1", "GDP_Q2", "GDP_Q3", "GDP_Q4"]].mean(axis=1)
data["Average_Inflation"] = data[["Inflation_Q1", "Inflation_Q2", "Inflation_Q3", "Inflation_Q4"]].mean(axis=1)

data.to_csv(output_processed_csv, index=False)
Step 3: Analysis and Reporting

For simplicity, let's generate a basic text-based report and a sample chart:

python
Copy code
import matplotlib.pyplot as plt

input_processed_csv = "processed_macroeconomic_data.csv"
output_report_file = "macroeconomic_report.txt"
output_chart_file = "gdp_inflation_chart.png"

data = pd.read_csv(input_processed_csv)

# Generate a basic report
report = "Macroeconomic Analysis Report\n\n"
report += "Year | Average GDP | Average Inflation\n"
report += "--------------------------------------\n"
for index, row in data.iterrows():
    report += f"{row['Year']} | {row['Average_GDP']} | {row['Average_Inflation']}\n"

with open(output_report_file, "w") as report_file:
    report_file.write(report)

# Generate a sample chart
plt.figure(figsize=(10, 6))
plt.plot(data["Year"], data["Average_GDP"], label="Average GDP")
plt.plot(data["Year"], data["Average_Inflation"], label="Average Inflation")
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Average GDP and Inflation Trends")
plt.legend()
plt.savefig(output_chart_file)
plt.close()


# In[ ]:


#Step3: Reporting and Analysis

import matplotlib.pyplot as plt

input_processed_csv = "processed_macroeconomic_data.csv"
output_report_file = "macroeconomic_report.txt"
output_chart_file = "gdp_inflation_chart.png"

data = pd.read_csv(input_processed_csv)

# Generate a basic report
report = "Macroeconomic Analysis Report\n\n"
report += "Year | Average GDP | Average Inflation\n"
report += "--------------------------------------\n"
for index, row in data.iterrows():
    report += f"{row['Year']} | {row['Average_GDP']} | {row['Average_Inflation']}\n"

with open(output_report_file, "w") as report_file:
    report_file.write(report)

# Generate a sample chart
plt.figure(figsize=(10, 6))
plt.plot(data["Year"], data["Average_GDP"], label="Average GDP")
plt.plot(data["Year"], data["Average_Inflation"], label="Average Inflation")
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Average GDP and Inflation Trends")
plt.legend()
plt.savefig(output_chart_file)
plt.close()


# In[ ]:




