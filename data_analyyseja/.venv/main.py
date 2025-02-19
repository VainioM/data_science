#tehdään analyyseja varten tarvittavat importit
import pandas as pd
from pathlib import Path
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

print("Data-analyysejä Pythonilla")
#§§
print("Tervetuloa")

titanic_df = pd.read_csv(Path().joinpath('titanic.csv')) #haetaan .csv-datasetti ja tallennetaan se muuttujaan titanic_df
print(titanic_df)

print(titanic_df.columns.values) #tarkistetaan sarakkaiden nimet

sample_titanic = titanic_df.sample(10)
sum_null = titanic_df.isnull().sum()

titanic_df_corr = pd.read_csv('titanic.csv', usecols=['Age', 'Pclass'], low_memory=True) #haetaan datasetistä sarakkeet 'Age' ja 'Pclass'

print(titanic_df_corr.corr()) #tutkitaan äsken haettujen sarakkeiden korrelaatiota keskenään. Niiden välinen korrelaatiokerroin on -0.37, eli muuttujat ovat kohtalaisessa negatiivisessa korrelaatiossa keskenään


print (titanic_df['Age'].mean()) #matkustajien ikien keskiarvo. Se on noin 29 vuotta

underaged_df = titanic_df.loc[titanic_df['Age'] <= 18] #haetaan alaikäisten matkustajien tiedot. Heitä on 139
#print(underaged_df)

survived_underaged_df = underaged_df.loc[underaged_df['Survived'] == 1] #tutkitaan kuinka moni heistä selviytyi. Heitä on 70, eli noin 50%
print(survived_underaged_df)

#funktio, joka luo palkkikaavion annettujen parametrien mukaan
def count_plot(x, hue, data):
    sns.countplot(x=x, hue=hue, data=data)
    plt.show()

#lähetetään funktiolle arvot 'survived' ja 'sex'
count_plot('Survived', 'Sex', titanic_df)

count_plot('Survived', 'Pclass', titanic_df)

