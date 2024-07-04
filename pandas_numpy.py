import numpy as np 
import pandas as pd

#ƒetch iris dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.describe())
#print(df.info())

#Selecting columns
print(df.columns)

#Selecting specific columns
#df_seleted = df[['species', 'petal_length', 'petal_width']]
#df_seleted.info()

#Filter rows by flower species
#df_setosa = df[df['species']=='setosa']
#df_setosa.info()

#Create new columns
df['petal_area'] = df['petal_length'] * df['petal_width']
#print(df.head())

#Renaming columns
df = df.rename(columns = {'petal_area' : 'petal_area (cm^2)'})
#print(df.head())

#Some calculations
print(df['petal_area (cm^2)'].mean())
print(df['species'].unique())

#Grouping
print(df.groupby('species')['petal_length'].std())

#Aggregating
print(df.groupby('species').agg(mean_petal_length=('petal_length', 'mean')))


import matplotlib.pyplot as plt
import matplotlib

print(matplotlib.__version__)