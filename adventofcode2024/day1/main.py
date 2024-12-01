import numpy as np


def leer_listas_de_archivo(nombre_archivo):
    """
    Lee un archivo .txt con pares de números y crea dos listas.

    Args:
        nombre_archivo: El nombre del archivo .txt.

    Returns:
        Una tupla de dos listas, cada una conteniendo los números de una columna.
    """

    lista1 = []
    lista2 = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            numero1, numero2 = map(int, linea.split())
            lista1.append(numero1)
            lista2.append(numero2)

    return lista1, lista2


def calculate_total_distance_numpy(list1, list2):
    # Convertir las listas a arreglos NumPy
    arr1 = np.array(list1)
    arr2 = np.array(list2)

    # Ordenar los arreglos
    arr1.sort()
    arr2.sort()

    # Calcular las diferencias absolutas y sumarlas
    return np.sum(np.abs(arr1 - arr2))


nombre_archivo = "input.txt"
lista1, lista2 = leer_listas_de_archivo(nombre_archivo)
result = calculate_total_distance_numpy(lista1, lista2)
print(result)  # Output: 11
