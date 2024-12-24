import pandas as pd

emissions = pd.read_csv('data/emissions.csv')
renewables = pd.read_csv('data/renewable.csv')
gdp = pd.read_csv('data/GDP.csv')

# print(renewables.head())
# print(emissions.head())
# print(gdp.head())

# emissions_columns = emissions.columns.tolist()
# renewables_columns = renewables.columns.tolist()
# gdp_columns = gdp.columns.tolist()

# print("Emissions Columns:", emissions_columns)
# print("Renewables Columns:", renewables_columns)
# print("GDP Columns:", gdp_columns)