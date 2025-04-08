import time

def bubble_sort(vetor):

    for i in range(0, len(vetor)):
        for j in range(0, len(vetor) - 1 - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def selection_sort(vetor, option):
    
    if option is 1:
        for i in range(0, len(vetor)):
            menor = i
            for j in range(i + 1, len(vetor)):
                if vetor[j] < vetor[menor]:
                    menor = j
            if i != menor:
                vetor[i], vetor[menor] = vetor[menor], vetor[i]
    elif option is 2:
        for i in range(0, len(vetor)):
            maior = i
            for j in range(i + 1, len(vetor)):
                if vetor[j] > vetor[maior]:
                    maior = j
            if i != maior:
                vetor[i], vetor[maior] = vetor[maior], vetor[i]
    else:
        print("Opção inválida")
    
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
selection_sort(vetor, 2)
fim = time.time()
print(vetor)
print(fim - inicio, "segundos")