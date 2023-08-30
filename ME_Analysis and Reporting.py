import matplotlib.pyplot as plt

# Load cleaned data from CSV
data = pd.read_csv("cleaned_macroeconomic_data.csv")

# Analysis: plot GDP over time
plt.plot(data["Year"], data["GDP"])
plt.xlabel("Year")
plt.ylabel("GDP")
plt.title("GDP Trends")
plt.savefig("gdp_trends.png")
plt.close()

# Generate a basic report
report = f"Macroeconomic Analysis Report\n\n"
report += "GDP Trends:\n"
report += "----------------\n"
report += "See attached GDP trends plot (gdp_trends.png)\n"

# Save the report to a text file
with open("macroeconomic_report.txt", "w") as f:
    f.write(report)
    
