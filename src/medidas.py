import pandas as pd
import numpy as np

def media_evolve(lista:list) -> float:
    """Calcula la media de una lista de números"""
    return round(sum(lista) / len(lista), 2)
def mediana_evolve(lista:list) -> float:
    """Calcula la mediana de una lista de números"""
    sorted_lista = sorted(lista)
    n = len(sorted_lista)
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
    media = media_evolve(lista)
    squared_diffs = [(x - media) ** 2 for x in lista]
    return round((sum(squared_diffs) / len(lista)) ** 0.5, 2)
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
if __name__=="__main__":
    np.random.seed(42) 
    df = pd.DataFrame({ 'edad': np.random.randint(20, 60, 100), 
                       'salario': np.random.normal(45000, 15000, 100),     
                       'experiencia': np.random.randint(0, 30, 100) })
    print("Percentil 0.20:", percentil_evolve(df['edad'],0.20))
    print("Percentil 0.80:", percentil_evolve(df['edad'],0.80))
    print("Media:", media_evolve(df['salario']))
    print("Mediana:", mediana_evolve(df['salario']))
    print("Desviación estándar:", desviacion_evolve(df['salario']))
    print("Rango intercuartílico:", IQR_evolve(df['salario']))
    print("Varianza:", varianza_evolve(df['salario']))