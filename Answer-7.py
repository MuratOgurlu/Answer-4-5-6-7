import pandas as pd


df = pd.read_csv("DataSet/country_vaccination_stats.csv")

dates = '1/6/2021'

#print(df[df['date'] == dates].head())

Sum = df[df['date'] == dates]['daily_vaccinations'].sum()

print(Sum)