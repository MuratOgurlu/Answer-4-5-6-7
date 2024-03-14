import pandas as pd

data = pd.read_csv("DataSet/country_vaccination_stats.csv")

data.fillna({"daily_vaccinations" : 0}, inplace=True)

data['date'] = pd.to_datetime(data['date'])

dataGroup = data.groupby('country')['daily_vaccinations'].median().reset_index()

dataGroupSorted = dataGroup.sort_values(by='daily_vaccinations', ascending=False)

top_3_countries = dataGroupSorted.head(3)

print(top_3_countries)