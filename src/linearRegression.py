def beta(x, y) -> float:
    somaXQuadrado = 0
    for xi in x:
        somaXQuadrado += xi**2
    sxx = somaXQuadrado - (sum(x) ** 2)/len(x)
    somaXY = 0
    for i in range(0, len(x)):
        somaXY += x[i] * y[i]
    sxy = somaXY - (sum(x) * sum(y))/len(x)
    return sxy / sxx

def alfa(x, y) -> float:
    midIndex = len(x) // 2
    return 5.82 - (beta(x, y) * 350.45)

def func(x: float) -> float:
    return 0.022822491012909084 * x - 2.178141975473988