def buscar_en_matriz(matriz, valor):
    """
    Busca un valor específico en una matriz bidimensional.

    :param matriz: Matriz en la que buscar.
    :param valor: Valor a buscar.
    :return: Tupla con las coordenadas (fila, columna) del valor, o None si no se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None



# Definición de la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 8

# Realiza la búsqueda
resultado = buscar_en_matriz(matriz, valor_a_buscar)

# Muestra el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")