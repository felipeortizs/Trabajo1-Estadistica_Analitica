import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definimos la función de densidad f(y)
def f(y, c=0.5):
    return c * y if 0 <= y <= 2 else 0

# Calculamos y graficamos f(y)
y_vals = np.linspace(0, 2, 100)
f_vals = [f(y) for y in y_vals]

plt.figure(figsize=(12, 5))

# Gráfica de f(y)
plt.subplot(1, 2, 1)
plt.plot(y_vals, f_vals, label='f(y) = 0.5y', color='blue')
plt.title('Función de Densidad f(y)')
plt.xlabel('y')
plt.ylabel('f(y)')
plt.grid(True)
plt.legend()

# Definimos la función de distribución acumulativa F(y)
def F(y):
    if y < 0:
        return 0
    elif 0 <= y <= 2:
        return (y ** 2) / 4
    else:
        return 1

# Calculamos y graficamos F(y)
F_vals = [F(y) for y in y_vals]

plt.subplot(1, 2, 2)
plt.plot(y_vals, F_vals, label='F(y) = y^2 / 4', color='green')
plt.title('Función de Distribución Acumulativa F(y)')
plt.xlabel('y')
plt.ylabel('F(y)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Calculamos la probabilidad P(1 <= Y <= 2) usando F(y)
P_1_2 = F(2) - F(1)

# Calculamos la probabilidad usando la integral
integral_result, _ = quad(f, 1, 2)

P_1_2, integral_result