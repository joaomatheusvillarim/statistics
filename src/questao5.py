import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt
import numpy
from scipy import stats

import linearRegression

x = [303.7, 366.7, 336.8, 304.5, 346.8, 600.0, 369.0, 418.0, 269.0, 323.0,
     562.2, 284.2, 558.6, 415.0, 349.5, 462.8, 333.1, 502.1, 311.4, 351.4]
y = [3.62, 7.27, 2.66, 1.53, 4.91, 10.36, 5.26, 6.09, 6.57, 4.24,
     8.04, 3.46, 8.5, 9.34, 5.55, 8.11, 7.32, 12.58, 0.15, 5.23]

#QUESTÃO 1: ANÁLISE DE REGRESSÃO LINEAR

#Estimação pontual e por intervalo dos coeficientes da regressão linear (β0, β1, ...)
print("O valor pontual de beta é", linearRegression.beta(x, y))
print("O valor pontual de alfa é", linearRegression.alfa(x, y))
xPoints = [269, 600.0]
yPoints = [3.961108106998555, 11.515352632271462]
plt.plot(x, y, 'o')
plt.plot(xPoints, yPoints)
plt.show()

#Estimação da variância, σ², do erro ε
erro = []
for i in range(0, 20):
    erro.append(linearRegression.func(x[i]) - y[i])
print("A variância do erro é de", stats.variation(erro))

#Obter o coeficiente de determinação, R², e interpretá-lo
beta, alfa, relacao, p, std_err = stats.linregress(x, y)
print("O coeficiente de determinação é", relacao)

#Fazer o gráfico da reta ajustada