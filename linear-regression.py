"""
Regressao linear para prever colocao nas competicoes nacionais 2017, 2018, 2019, 2020 baseado nas notas das areas de projeto, dinamica e enduro 
"""

import webscrap
import pandas as pd

"""
Importando os dataframes do script: webscrap.py e agrupando em um unico
"""
frames = [webscrap.df_2017, webscrap.df_2018, webscrap.df_2019, webscrap.df_2020]
df = pd.concat(frames)

"""
Dividindo os dados de treino e teste
"""

from sklearn.model_selection import train_test_split

Y = df['rank']
X = df.drop(columns=['rank'])

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.23)

"""
Aplicando o algoritmo de regressao linear
"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

"""
Resultados previstos/Metricas
"""

print('Coeficientes:', model.coef_)
print('Erro quadratico medio(MSE): %.4f' % mean_squared_error(Y_test, Y_pred))
#print('Raiz do erro quadratico medio(RMSE): %.4f' % )
print('Coeficiente de determinacao(R^2): %.4f' % r2_score(Y_test, Y_pred))

"""
Grafico de pontos Y_test,Y_pred
"""

import matplotlib.pyplot as plt

plt.scatter(Y_test,Y_pred, alpha=0.5)
plt.xlabel("Resultados reais")
plt.ylabel("Resultados previsto")
plt.title("")
#plt.savefig('real/previsto.png', format='png')

pred = model.predict([[237, 118, 325]])
print('Classificacao esperada: %.2f' % pred)