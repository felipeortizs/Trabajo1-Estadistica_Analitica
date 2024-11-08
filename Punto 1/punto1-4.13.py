import numpy as np
from scipy.integrate import quad

# Definimos la función f(y) para los intervalos dados
def f(y):
    if 0 <= y <= 1:
        return y
    elif 1 < y <= 1.5:
        return 1
    else:
        return 0

# Función de distribución acumulativa F(y)
def F(y):
    if y < 0:
        return 0
    elif 0 <= y <= 1:
        return y**2 / 2
    elif 1 < y <= 1.5:
        return 0.5 + (y - 1)
    else:
        return 1

# Cálculo de F(0.5)
F_0_5 = F(0.5)

# Cálculo de F(1.2)
F_1_2 = F(1.2)

# Probabilidad P(0 <= Y <= 0.5)
P_0_5 = F_0_5

# Probabilidad P(0.5 <= Y <= 1.2)
P_0_5_to_1_2 = F_1_2 - F_0_5

F_0_5, F_1_2, P_0_5, P_0_5_to_1_2

