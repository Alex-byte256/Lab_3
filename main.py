import pandas
import numpy as np
import matplotlib.pyplot as plt

empl = pandas.read_csv('employees.csv')
nba = pandas.read_csv('nba.csv')

print(empl.isnull())
empl.replace('', np.nan)
empl.dropna()
print(empl.isnull())

nba.replace('', np.nan)
nba.dropna()
print(nba['Height'].head())
nba['Height'] = nba['Height'].str.replace('-', '.')

print(nba['Weight'].head())
nba['Weight'] *= 0.45359237
print(nba['Weight'].head())

nba['Height'] = pandas.to_numeric(nba['Height'], downcast='float')
nba['Height'] /= 3.28084
print(nba['Height'].head())

print(empl['First Name'].count())
print(nba['Name'].count())

print(empl['Salary'].max())
print(nba['Weight'].max())

print(empl['Salary'].mean())
print(nba['Weight'].mean())

columns = ['Age', 'Weight']
values = [nba['Age'].mean(), nba['Weight'].mean()]
plt.bar(columns, values)
plt.title('Nba-dataset')
plt.xlabel('Column')
plt.ylabel('Mean value')
plt.show()