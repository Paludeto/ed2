import random
# vetor = [random.randrange(100) for _ in range(10)]

# print("Vetor gerado:")
# print('[ ', end='')
# for i in vetor:
#     print(i, end=' ')
# print(']')

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def busca_linear(array, elemento):
    for i in range(0, len(array) - 1):
        if array[i] is elemento:
            return i
    return -1

def busca_binaria(array, elemento, inicio, fim):
    
    if inicio > fim:
        return -1
    
    meio = inicio + (fim - inicio) // 2
    
    if array[meio] == elemento:
        return meio
    elif array[meio] < elemento:
        return busca_binaria(array, elemento, meio + 1, fim)
    else:
        return busca_binaria(array, elemento, inicio, meio - 1)

print(busca_linear(vetor, 5))
print(busca_binaria(vetor, 11, 0, len(vetor) - 1))