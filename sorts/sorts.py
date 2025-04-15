import time

def bubble_sort(vetor):

    for i in range(0, len(vetor)):
        for j in range(0, len(vetor) - 1 - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def selection_sort(vetor, option):
    
    if option == 1:
        for i in range(0, len(vetor) - 1):
            menor = i
            for j in range(i + 1, len(vetor)):
                if vetor[j] < vetor[menor]:
                    menor = j
            if i != menor:
                vetor[i], vetor[menor] = vetor[menor], vetor[i]
    elif option == 2:
        for i in range(0, len(vetor) - 1):
            maior = i
            for j in range(i + 1, len(vetor)):
                if vetor[j] > vetor[maior]:
                    maior = j
            if i != maior:
                vetor[i], vetor[maior] = vetor[maior], vetor[i]
    else:
        print("Opção inválida")

def insertion_sort(vetor):

    for i in range(1, len(vetor)):
        
        k = i - 1   # Antecede i
        aux = vetor[i]
        
        # Move elementos maiores para a direita enquanto o elemento da direita é menor do que o da esquerda
        while k >= 0 and aux < vetor[k]:
            vetor[k + 1] = vetor[k]
            k = k - 1
        vetor[k + 1] = aux

# Tempo Bubblesort
print("Bubblesort")
vetor = [-93, 97, -92, 69, -7, 6, 94, 53, 35, -34, 0, -14, -26, 32, 87]
inicio = time.time()
bubble_sort(vetor)
fim = time.time()
print(vetor)
print(fim - inicio, "segundos")

# Tempo Selection Sort
print("Selection sort")
vetor = [-93, 97, -92, 69, -7, 6, 94, 53, 35, -34, 0, -14, -26, 32, 87]
inicio = time.time()
selection_sort(vetor, 1)
fim = time.time()
print(vetor)
print(fim - inicio, "segundos")

# Insertion sort
print("Insertion sort")
vetor = [-93, 97, -92, 69, -7, 6, 94, 53, 35, -34, 0, -14, -26, 32, 87]
inicio = time.time()
insertion_sort(vetor)
fim = time.time()
print(vetor)
print(fim - inicio, "segundos")