import pandas as pd

data = pd.read_csv("Dataset/country_vaccination_stats.csv")

data.fillna({"daily_vaccinations" : 0}, inplace=True)

print(data.head())