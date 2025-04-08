import time

def bubble_sort(vetor):

    n = len(vetor) - 1

    for i in range(0, n):
        for j in range(0, n - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def selection_sort(vetor):
    
    for i in range(0, len(vetor)):
        menor = i
        for j in range(i + 1, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
        if i != menor:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]

# Tempo Bubblesort
print("Bubblesort")
vetor = list(range(10**1, 0, -1))
inicio = time.time()
bubble_sort(vetor)
fim = time.time()
print(vetor)
print(fim - inicio, "segundos")

# Tempo Selection Sort
vetor = [8, 4, 3, 2, 19, 0]
inicio = time.time()
selection_sort(vetor)
fim = time.time()
print(vetor)
print(fim - inicio, "segundos")