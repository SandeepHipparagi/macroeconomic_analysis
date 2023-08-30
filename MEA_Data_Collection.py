#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# Example URL for data source
data_source_url = "https://datacatalog.worldbank.org/dataset/worlddevelopment-indicators"

# Fetch data from the source
response = requests.get(data_source_url)
data = response.json()  # Assuming the data is in JSON format

# Save data to a CSV file
with open("macroeconomic_data.csv", "w") as f:
    for entry in data:
        f.write(",".join(entry.values()) + "\n")


# In[ ]:




