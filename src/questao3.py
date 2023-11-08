import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt
import numpy
from scipy import stats

x = [303.7, 366.7, 336.8, 304.5, 346.8, 600.0, 369.0, 418.0, 269.0, 323.0,
     562.2, 284.2, 558.6, 415.0, 349.5, 462.8, 333.1, 502.1, 311.4, 351.4]
y = [3.62, 7.27, 2.66, 1.53, 4.91, 10.36, 5.26, 6.09, 6.57, 4.24,
     8.04, 3.46, 8.5, 9.34, 5.55, 8.11, 7.32, 12.58, 0.15, 5.23]

#QUESTÃO 3: TESTES DE HIPÓTESES

indexes = numpy.random.randint(0, 19, 5)
sampleFromX, sampleFromY = [], []
for index in indexes:
    sampleFromX.append(x[index])
indexes = numpy.random.randint(0, 19, 5)
for index in indexes:
    sampleFromY.append(y[index])

#testes de hipóteses sobre a média da resposta
print("---TESTE 1---")
print("Selecionando aleatoriamente uma amostra do conjunto de observações" +
      " da variável X, vamos usar um teste de T-Student para determinar se" +
      " a média da amostra é igual à media da população.")
print("Hipótese nula: A média da amostra é de 388.39\n" +
      "Hipótese alternativa: as médias da amostra e da população são" +
      " diferentes.")
estatisticaT, valorP = stats.ttest_1samp(sampleFromX, 388.39)
print("A estatística do teste é de", estatisticaT)
print("O valor P é de", valorP)
conclusao = "Não rejeitar a hipótese nula"
if valorP < 0.05:
    conclusao = "Rejeitar a hipótese nula"
print(conclusao)

#testes de hipóteses sobre a variância da resposta
print("---TESTE 2---")
print("Dado que o conjunto dos valores X e Y das observações possuem o mesmo" +
      " tamanho, podemos utilizar um teste de qui-quadrado para determinar se" +
      " suas variâncias são iguais.")
print("Hipótese nula: As variâncias de X e Y são iguais\n" +
      "Hipótese alternativa: As variâncias de X e Y são diferentes")
data = [x, y]
stat, valorP, dof, expected = stats.chi2_contingency(data)
print("O valor P é de", valorP)
conclusao = "Não rejeitar a hipótese nula"
if valorP < 0.05:
    conclusao = "Rejeitar a hipótese nula"
print(conclusao)
