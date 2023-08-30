import requests

# URL for data source
data_source_url = "https://datacatalog.worldbank.org/dataset/worlddevelopment-indicators"

# Fetch data from the source
response = requests.get(data_source_url)
data = response.json() 

# Save data to a CSV file
with open("macroeconomic_data.csv", "w") as f:
    for entry in data:
        f.write(",".join(entry.values()) + "\n")
