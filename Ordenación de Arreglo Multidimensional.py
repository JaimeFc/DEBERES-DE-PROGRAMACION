def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, num_fila):
    bubble_sort(matriz[num_fila])

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Creación de la matriz 3x3
matriz = [
    [5, 3, 2],
    [8, 5, 1],
    [4, 7, 6]
]

print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar una fila específica, por ejemplo, la fila 1 (segunda fila)
ordenar_fila(matriz, 1)

print("\nMatriz con la fila ordenada:")
imprimir_matriz(matriz)