import numpy as np
import pandas as pd

# Definimos el nuevo estimador de la media
def nuevo_estimador(x):
    n = len(x)
    return (100 * n / (n**2 + 1)) + (np.sum(x) / n)

# Definimos el estimador habitual (media muestral)
def estimador_habitual(x):
    return np.mean(x)

# Simulamos datos de una distribución normal con media 50 y varianza 10
tamaños_muestra = [10, 100, 1000, 10000, 100000]
media = 50
desviacion_estandar = np.sqrt(10)

# Calculamos las estimaciones y las guardamos en una lista
resultados = []
for n in tamaños_muestra:
    muestra = np.random.normal(media, desviacion_estandar, n)
    estimacion_nueva = nuevo_estimador(muestra)
    estimacion_habitual = estimador_habitual(muestra)
    resultados.append((n, estimacion_nueva, estimacion_habitual))

# Convertimos los resultados en un DataFrame
df_resultados = pd.DataFrame(resultados, columns=["Tamaño de muestra", "Estimador nuevo", "Estimador habitual"])

# Mostramos el DataFrame
print(df_resultados)
