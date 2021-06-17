import pandas as pd
import seaborn as sb
import matplotlib as mpl
import numpy as np

sales = pd.read_csv('./data_csv/sales_predictions.csv')
sales.head()

sales.describe()

# 2) En utilisant relplot(), construisez un graphique qui va vous permettre de voir l’évolution des prix par rapport au temps. Que pouvez vous voir ?
sb.relplot(x='date', y='item_price', data=sales)

# 3) Corrigeons le problème de visualisation, en utilisant la fonction .sample() de Pandas, prenez un échantillons de 50 éléments dans votre dataset
sales_sample = sales.sample(50, replace=True)
sb.relplot(x='date', y='item_price', data=sales_sample)

# 4) Retentez de faire votre visualisation et créer une figure plus grande. Que voyez vous ?
sb.relplot(x='date', y='item_price', data=sales_sample, height=8, aspect=3)

# 5) En utilisant la fonction pd.to_datetime(), convertissez votre colonne date en datetime
sales_sample['date'] = pd.to_datetime(sales_sample['date'])

# 6) Retentez une dernière fois votre visualisation.
sb.relplot(x='date', y='item_price', data=sales_sample, height=8, aspect=3)
