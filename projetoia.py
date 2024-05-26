# -*- coding: utf-8 -*-
"""ProjetoIA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZNUGRAsCvng9iM680rihSgKApIzFY9fM
"""

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import numpy as np

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import statsmodels.api as sm



#importando dataframe
dataframe = pd.read_csv("/content/bottle.csv", on_bad_lines='skip')
#Mostrando colunas
dataframe.columns

#Mostrando informações do dataframe
dataframe.info()

#Mostrando 5 primeiras linhas do dataframe
dataframe.head()

#Verificando se há valores vazios
df = dataframe

df.isnull().values.any()

#Removendo linhas com valores vazios
df = df.dropna()

#Alterando nome das colunas que serão utilizadas
df = dataframe.rename(columns ={'T_degC':'Temperatura', 'Salnty': 'Salinidade'})
df = df[['Temperatura','Salinidade']]
df.head()

scaler = StandardScaler()

# Aplicando o método fit_transform() do objeto scaler nos dados do DataFrame df
# Ajusta a escala dos dados
scaled_data = scaler.fit_transform(df)

# Removendo as linhas que contêm valores NaN (valores ausentes) do array de dados escalonados
# Utilizando a função numpy np.isnan() para identificar valores NaN e a função any(axis=1) para identificar linhas que contenham pelo menos um valor NaN
scaled_data_sem_nan = scaled_data[~np.isnan(scaled_data).any(axis=1)]

# Dividindo os dados em conjuntos de treinamento e teste
x_train, x_test, y_train, y_test = train_test_split(scaled_data_sem_nan[:,0], scaled_data_sem_nan[:,1], test_size=0.30, random_state=42)

#Aplicação da regressão linear e treino do modelo

ia = LinearRegression()

ia.fit(x_train.reshape(-1,1), y_train)

y_hat = ia.predict(x_test.reshape(-1,1))

# Calcular R²
r2 = r2_score(y_test, y_hat)

# Calcular MAE
mae = mean_absolute_error(y_test, y_hat)

# Calcular MSE
mse = mean_squared_error(y_test, y_hat)

# Calcular RMSE
rmse = np.sqrt(mse)
print(y_hat[:10])
print(y_test[:10])

print(f'R²: {r2:.2f}')
print(f'MAE: {mae:.2f}')
print(f'MSE: {mse:.2f}')
print(f'RMSE: {rmse:.2f}')

plt.figure(figsize=(8, 6))
sns.regplot(x='Temperatura', y='Salinidade', data=df, ci=None, scatter_kws={'color':'green'}, line_kws={'color':'red'})
plt.title('Regressão Linear')
plt.xlabel('Temperatura')
plt.ylabel('Salinidade')
plt.grid(True)
plt.show()

print("Coeficiente linear (intercept):", ia.intercept_)
print("Coeficiente angular (slope):", ia.coef_)
