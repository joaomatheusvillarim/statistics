import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt
import numpy
from scipy import stats

x = [303.7, 366.7, 336.8, 304.5, 346.8, 600.0, 369.0, 418.0, 269.0, 323.0,
     562.2, 284.2, 558.6, 415.0, 349.5, 462.8, 333.1, 502.1, 311.4, 351.4]
y = [3.62, 7.27, 2.66, 1.53, 4.91, 10.36, 5.26, 6.09, 6.57, 4.24,
     8.04, 3.46, 8.5, 9.34, 5.55, 8.11, 7.32, 12.58, 0.15, 5.23]

#QUESTÃO 1: ESTATÍSTICA DESCRITIVA

#MEDIDAS DE RESUMO
#média
print("A média da variável X é", numpy.mean(x))
print("A média da variável Y é", numpy.mean(y).round(4))
#moda
print("A moda da variável X é, calculada pelo programa é", *stats.mode(x).mode,
      "que ocorre um total de", *stats.mode(x).count, "vez, o que torna a amostra" +
      "observada amodal")
print("A moda da variável Y é, calculada pelo programa é", *stats.mode(y).mode,
      "que ocorre um total de", *stats.mode(y).count, "vez, o que torna a amostra" +
      " observada amodal")
#mediana
print("A mediana da variável X é", numpy.median(x))
print("A mediana da variável Y é", numpy.median(y))
#variância
print("A variância da variável X é de", stats.variation(x))
print("A variância da variável Y é de", stats.variation(y))
#desvio padrão
print("O desvio padrão da variável X é de", numpy.std(x))
print("O desvio padrão da variável Y é de", numpy.std(y))
#coeficiente de correlação

#REPRESENTAÇÃO GRÁFICA

#histograma

plt.hist(x, edgecolor="black")
plt.show()
plt.hist(y, edgecolor="black")
plt.show()

#box-plot
plt.boxplot(x)
plt.show()
plt.boxplot(y)
plt.show()

#gráfico de dispersão
plt.plot(x, y, 'o')
plt.show()