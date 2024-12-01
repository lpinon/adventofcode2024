
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


nombre_archivo = "input.txt"
lista1, lista2 = leer_listas_de_archivo(nombre_archivo)

cantidades = {}

for e in lista2:
    if e not in cantidades.keys():
        cantidades[e] = 0
    cantidades[e] += 1

total = 0
for e in lista1:
    if e in cantidades.keys():
        total += e * cantidades[e]

print(total)
