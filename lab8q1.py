import numpy as np
import matplotlib.pyplot as plt


covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100],  # Day 7
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Task 1: Basic Statistics
# Total cases per country
total_cases_per_country = covid_data.sum(axis=0)
highest_total_cases_country = countries[np.argmax(total_cases_per_country)]

# Task 2: Daily Analysis
# Average daily cases across all countries
average_daily_cases = covid_data.mean(axis=1)
day_with_highest_cases = np.argmax(covid_data.sum(axis=1)) + 1

# Task 3: Trends
# Percentage change from Day 1 to Day 7 for each country
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
highest_percentage_increase_country = countries[np.argmax(percentage_change)]

# Task 4: Data Transformation
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))

# Visualization: Line chart of daily cases
plt.figure(figsize=(12, 6))
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], label=country, marker='o')

# Highlight the day with the highest total cases
plt.axvline(x=day_with_highest_cases, color='red', linestyle='--', label=f"Highest Cases Day {day_with_highest_cases}")
plt.title("Daily COVID-19 Cases for Each Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.xticks(range(1, 8))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Outputs for analysis
print("Total Cases Per Country:", total_cases_per_country)
print("Country with Highest Total Cases:", highest_total_cases_country)
print("Average Daily Cases Across All Countries:", average_daily_cases)
print("Day with Highest Total Cases:", day_with_highest_cases)
print("Percentage Change Per Country:", percentage_change)
print("Country with Highest Percentage Increase:", highest_percentage_increase_country)
print("Normalized Dataset:\n", normalized_data)
