import pandas as pd
import seaborn as sb
import matplotlib as mpl
import numpy as np

# 2) Donnez la liste des variables présentes dans ce dataset ainsi que leur nature (sont elles qualitatives, quantitatives, discrète etc…) et leur type (float, int, str etc…)
data = pd.read_csv("./data_csv/house_pricing.csv")

data.head()


# 3) En créant un nuage de points, regardez comment se comporte la colonne LotArea par rapport au SalesPrices
df = data[(data['SalePrice'] < 500000) & (data['LotArea'] < 20000)]
sb.scatterplot(x='SalePrice', y='LotArea', data=df)


# 4) Affinez votre visualisation en ne gardant uniquement les maisons qui ont un LotArea inférieur à 20 000 pieds carrés et un prix inférieur à 500 000$


# 5) En créant un nuage de points, regardez la relation entre le LotFrontage et le LotArea


# 6) De la même manière, affinez votre visualisation en ne gardant uniquement les maisons qui ont un LotFrontage inférieur à 200 pieds carrés et un LotArea inférieur à 100000 pieds carré
