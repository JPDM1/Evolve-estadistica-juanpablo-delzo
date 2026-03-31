import pandas as pd
import numpy as np

def media_evolve(lista:list) -> float:
    """Calcula la media de una lista de números"""
    return round(sum(lista) / len(lista), 2)

def mediana_evolve(lista:list) -> float:
    """Calcula la mediana de una lista de números"""
    sorted_lista = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        return (sorted_lista[n//2 - 1] + sorted_lista[n//2]) / 2
    else:
        return sorted_lista[n//2]
    
def percentil_evolve(lista:list, percentil:float) -> float:
    """Calcula el percentil de una lista de números"""
    sorted_lista = sorted(lista)
    n = len(lista)
    k=round(percentil *n, 0)
    return sorted_lista[int(k)-1]

def desviacion_evolve(lista:list) -> float:
    """Calcula la desviación estándar de una lista de números"""
    return round(varianza_evolve(lista) ** 0.5, 2)

def IQR_evolve(lista:list) -> float:
    """Calcula el rango intercuartílico de una lista de números"""
    q1 = percentil_evolve(lista, 0.25)
    q3 = percentil_evolve(lista, 0.75)
    return q3 - q1

def varianza_evolve(lista:list) -> float:
    """Calcula la varianza de una lista de números"""
    media = media_evolve(lista)
    squared_diffs = [(x - media) ** 2 for x in lista]
    return round(sum(squared_diffs) / len(lista), 2)

def numero_outlier_evolve(lista:list) -> int:
    """Calcula el número de outliers en una lista de números"""
    iqr = IQR_evolve(lista)
    q1 = percentil_evolve(lista, 0.25)
    q3 = percentil_evolve(lista, 0.75)
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in lista if x < lower_bound or x > upper_bound]
    return len(outliers)

def skewness_evolve(lista:list) -> float:
    """Calcula la asimetría de una lista de números"""
    media = media_evolve(lista)
    desviacion = desviacion_evolve(lista)
    n = len(lista)
    if desviacion == 0:
        return 0
    skewness = (sum((x - media) ** 3 for x in lista) / n) / (desviacion ** 3)
    return round(skewness, 2)

def kurtosis_evolve(lista:list) -> float:
    """Calcula la curtosis de una lista de números"""
    media = media_evolve(lista)
    desviacion = desviacion_evolve(lista)
    n = len(lista)
    if desviacion == 0:
        return 0
    else:
        kurtosis = (sum((x - media) ** 4 for x in lista) / n) / (desviacion ** 4)
        return round(kurtosis, 2)

if __name__=="__main__":
    np.random.seed(39) 
    df = pd.DataFrame({ 'edad': np.random.randint(20, 60, 101), 
                       'salario': np.random.normal(45000, 15000, 101),     
                       'experiencia': np.random.randint(0, 30, 101) })
    print(df.describe())
    print("Percentil 0.20:", percentil_evolve(df['edad'],0.20))
    print("Percentil 0.80:", percentil_evolve(df['edad'],0.80))
    print("Media:", media_evolve(df['salario']))
    print("Mediana:", mediana_evolve(df['salario']))
    print("Desviación estándar:", desviacion_evolve(df['salario']))
    print("Rango intercuartílico:", IQR_evolve(df['salario']))
    print("Varianza:", varianza_evolve(df['salario']))
    print("Número de outliers:", numero_outlier_evolve(df['salario']))
    print("Asimetría:", skewness_evolve(df['salario']))
    print("Curtosis:", kurtosis_evolve(df['salario']))