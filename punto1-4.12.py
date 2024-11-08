import math

# Cálculo de phi_0.30
phi_30 = math.sqrt(-math.log(0.70))

# Función de densidad de probabilidad f(y)
def f(y):
    return 2 * y * math.exp(-y**2) if y >= 0 else 0

# Probabilidad de que Y >= 2
P_Y_ge_2 = math.exp(-4)

# Probabilidad condicional P(Y > 1 | Y <= 2)
P_1_less_Y_le_2 = math.exp(-1) - math.exp(-4)
P_Y_le_2 = 1 - math.exp(-4)
P_Y_gt_1_given_Y_le_2 = P_1_less_Y_le_2 / P_Y_le_2

phi_30, P_Y_ge_2, P_Y_gt_1_given_Y_le_2
