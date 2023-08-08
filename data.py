import pandas as pd

data = pd.read_csv('US_inflation_rates.csv')

data.dropna(inplace=True)

data['date'] = pd.to_datetime(data['date'])

print (data.describe)

data.to_csv("cleaned_data.csv", index=False)
