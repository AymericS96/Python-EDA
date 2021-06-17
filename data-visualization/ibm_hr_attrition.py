import pandas as pd
import seaborn as sb
import matplotlib as mpl
import numpy as np

attrition = pd.read_csv('./data_csv/IBM_HR_ATTRITION.csv')
pd.set_option('display.max_columns', 100)
attrition.head()

# 2) En utilisant catplot(), construisez un graphique qui vous permette de voir la distribution des personnes qui ont quitté l’entreprise par rapport à leur JobSatisfaction
sb.catplot(x='JobSatisfaction', y='Attrition', data=attrition)

# 3) Changez de graphique et utilisez plutôt un boxplot, que pouvez vous conclure ?
sb.boxplot(x='JobSatisfaction', y='Attrition', data=attrition)
# Le boxplot permet de tirer des conclusions là où le catplot ne nous apportait rien.

# 4) Peut-on dire grâce aux boxplot si une variable présente des valeurs aberrantes ?


# 5) Isolez les observations présentant des valeurs aberrantes pour la variable JobSatisfaction en fonction de la variable indiquant si ils ont quitté l’entreprise ou nom
filtered_attrition = attrition[(attrition['Attrition'] == 'Yes') &
                               (attrition['JobSatisfaction'] >= 2.5)]
sb.boxplot(x='JobSatisfaction', y='Attrition', data=filtered_attrition)

# 6) Utilisez la méthode .describe de pandas pour obtenir un tableau récapitulatif des statistiques descriptives du dataset.
attrition.describe()


# 7) Comparez les individus présentant des valeurs aberrantes pour la variable JobSatisfaction avec les statistiques descriptives du dataset, remarquez-vous des différences notoires ?


# 8) Faites de même avec le TotalWorkingYears. Que pouvez vous conclure ?


# 9) Remplacer les valeurs de la colonne Attrition par 1 pour Yes et 0 pour No


# 10) En utilisant un Histogramme, regardez la répartition du taux de départ par EducationField
