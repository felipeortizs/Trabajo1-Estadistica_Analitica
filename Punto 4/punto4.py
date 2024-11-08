import numpy as np
import pandas as pd

# Parámetros
p_real = 0.5  # Valor real de p
tamaños_muestra = [10, 50, 100, 500, 1000, 5000]  # Diferentes tamaños de muestra
num_simulaciones = 1000  # Número de simulaciones para cada tamaño de muestra

# Almacenaremos los promedios de los estimadores para cada tamaño de muestra
resultados = []

# Simulación para cada tamaño de muestra
for n in tamaños_muestra:
    estimaciones_hat_p = []  # Para almacenar los valores de \hat{p}
    estimaciones_tilde_p = []  # Para almacenar los valores de \tilde{p}
    
    # Simulaciones
    for _ in range(num_simulaciones):
        # Generamos una muestra binomial con tamaño de muestra n y probabilidad p_real
        Y = np.random.binomial(n, p_real)
        
        # Calculamos los estimadores
        hat_p = Y / n
        tilde_p = (Y + 1) / (n + 2)
        
        # Almacenamos los resultados de cada estimación
        estimaciones_hat_p.append(hat_p)
        estimaciones_tilde_p.append(tilde_p)
    
    # Calculamos los promedios de los estimadores
    promedio_hat_p = np.mean(estimaciones_hat_p)
    promedio_tilde_p = np.mean(estimaciones_tilde_p)
    
    # Guardamos los resultados para el tamaño de muestra actual
    resultados.append((n, promedio_hat_p, promedio_tilde_p))

# Convertimos los resultados a un DataFrame para visualizar
df_resultados = pd.DataFrame(resultados, columns=["Tamaño de muestra", "Promedio \hat{p}", "Promedio \tilde{p}"])

# Mostramos el DataFrame
df_resultados

