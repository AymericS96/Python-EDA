import pandas as pd
import seaborn as sb
import matplotlib as mpl
import numpy as np

################################################################
# Visualisation de variables catégoriques
################################################################

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
                               (attrition['JobSatisfaction'])]
sb.boxplot(x='Attrition', y='JobSatisfaction', data=filtered_attrition)

# 6) Utilisez la méthode .describe de pandas pour obtenir un tableau récapitulatif des statistiques descriptives du dataset.
attrition.describe()


# 7) Comparez les individus présentant des valeurs aberrantes pour la variable JobSatisfaction avec les statistiques descriptives du dataset, remarquez-vous des différences notoires ?


# 8) Faites de même avec le TotalWorkingYears. Que pouvez vous conclure ?
sb.catplot(x='TotalWorkingYears', y='Attrition', data=attrition)
sb.boxplot(x='TotalWorkingYears', y='Attrition', data=attrition)

filtered_attrition2 = attrition[(attrition['Attrition'] == 'Yes') &
                                (attrition['TotalWorkingYears'])]
sb.boxplot(x='Attrition', y='TotalWorkingYears', data=filtered_attrition2)

# On observe aussi des valeurs aberrantes pour l'ancienneté donc il n'y a pas de corrélation entre cette variable et le départ des employés.

# 9) Remplacer les valeurs de la colonne Attrition par 1 pour Yes et 0 pour No
attrition2 = pd.read_csv('./data_csv/IBM_HR_ATTRITION.csv')
attrition2['Attrition'] = attrition2['Attrition'].replace({"No": 0, "Yes": 1})
sb.boxplot(x='Attrition', y='TotalWorkingYears', data=attrition2)

# 10) En utilisant un Histogramme, regardez la répartition du taux de départ par EducationField
sb.catplot(x='EducationField', y='Attrition',
           data=attrition2, kind='bar', height=7, aspect=3)


################################################################
# Visualisation d’une distribution
################################################################

# 2) En utilisant displot(), construisez un graphique qui permette de voir la distribution des revenues par mois chez IBM (MonthlyIncome)


# 3) On peut voir que les très haut salaires biaisent notre distribution, essayons de voir la distribution des salaires entre 0 et 5000$ / mois


################################################################
# Visualisation d’une relation linéaire
################################################################

# 2) On voudrait connaître la probabilité de partir de la l’entreprise par rapport à la distance par rapport à la maison. Utilisez lmplot() pour visualiser cela. Que pouvez vous conclure ?


# 3) Tentez le cette fois avec le nombre d’années passées avec le Manager (YearsWithCurrManager), que pouvez vous conclure ?
