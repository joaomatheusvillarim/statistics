import matplotlib.pyplot as plt
import numpy
from scipy import stats
from scipy.stats import t

y = [3.62, 7.27, 2.66, 1.53, 4.91, 10.36, 5.26, 6.09, 6.57, 4.24, # Dano no fruto 
     8.04, 3.46, 8.5, 9.34, 5.55, 8.11, 7.32, 12.58, 0.15, 5.23]

x = [303.7, 366.7, 336.8, 304.5, 346.8, 600.0, 369.0, 418.0, 269.0, 323.0,  #  Altura de Queda
     562.2, 284.2, 558.6, 415.0, 349.5, 462.8, 333.1, 502.1, 311.4, 351.4]

#QUESTÃO 2: ESTIMAÇÃO PONTUAL E POR INTERVALO

#Estimação pontual da média
print("A média da altura de queda é", numpy.mean(x).round(2))
print("A média do dano no fruto é", numpy.mean(y).round(2))

#Estimação por intervalo da média

print("Com 95% de confiança, a média populacional da altura de queda está contida no intervalo", numpy.percentile(x, [2.5, 97.5]))
print("Com 95% de confiança, a média populacional do dano no fruto está contida no intervalo", numpy.percentile(y, [2.5, 97.5]))

#Estimação pontual da variância
print("A variância do dano no fruto é", numpy.var(y, ddof=1).round(2))
print("A variância da altura de queda é", numpy.var(x, ddof=1).round(2))

#Estimação por intervalo da variância
print("Intervalo de confiança da variância da altura de queda (95%):", [(numpy.var(y, ddof=1) * t.ppf(0.025, len(y) - 1)).round(2), (numpy.var(y, ddof=1) * t.ppf(0.975, len(y) - 1)).round(2)])
print("Intervalo de confiança da variância do dano no fruto (95%):", [(numpy.var(y, ddof=1) * t.ppf(0.025, len(x) - 1)).round(2), (numpy.var(x, ddof=1) * t.ppf(0.975, len(x) - 1)).round(2)] )
