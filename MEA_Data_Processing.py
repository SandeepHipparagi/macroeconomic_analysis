import pandas as pd

# Load data from CSV
data = pd.read_csv("macroeconomic_data.csv")

# Perform data preprocessing and cleaning (e.g., handling missing values)
data.fillna(0, inplace=True)  # Filling missing values with zeros

# Save cleaned data to a new CSV
data.to_csv("cleaned_macroeconomic_data.csv", index=False)
