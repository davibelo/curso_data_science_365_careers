import pandas as pd
import seaborn as sns

data = pd.read_csv('Country clusters standardized.csv', index_col='Country')

x_scaled = data.copy()
x_scaled = x_scaled.drop(['Language'],axis=1)

x_scaled

sns.clustermap(x_scaled, cmap='mako')
