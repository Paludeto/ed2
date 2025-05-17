# Autor: Gabriel Paludeto, RA 2605643

import sys          # => argc e argv
import time         # => profiling
import requests     # => chamadas para API
import random       # => métodos pseudoaleatórios
import math         # => funções matemáticas

# Dict que mapeia nome da função a número de comparações correspondentes
comparacoes = {
    "Bubble Sort": 0,
    "Selection Sort": 0,
    "Insertion Sort": 0,
    "Heap Sort": 0,
    "Quick Sort": 0,
    "Charizard Sort": 0
}

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            comparacoes["Bubble Sort"] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes["Selection Sort"] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes["Insertion Sort"] += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = chave

# Heapsort
def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n:
        comparacoes["Heap Sort"] += 1
        if arr[esq] > arr[maior]:
            maior = esq
    if dir < n:
        comparacoes["Heap Sort"] += 1
        if arr[dir] > arr[maior]:
            maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Quicksort (versão iterativa para não estourar call stack)
def particiona(arr, inicio, fim):
    pivo_idx = random.randint(inicio, fim)
    arr[pivo_idx], arr[fim] = arr[fim], arr[pivo_idx]

    pivo = arr[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        comparacoes["Quick Sort"] += 1
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

def quicksort_iterativo(arr, inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
    pilha = [(inicio, fim)]

    while pilha:
        inicio, fim = pilha.pop()
        if inicio < fim:
            p = particiona(arr, inicio, fim)
            pilha.append((inicio, p - 1))
            pilha.append((p + 1, fim))

# Charizard Sort, método de ordenação autoral
def charizard_sort(arr):
    id = random.randint(1, 251) # Gera ID aleatório de 1 a 251 (primeiras duas gerações de pokémon)
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"

    try:    # Tenta fazer um request utilizando a API
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Erro no request:", e)
        return None

    # Se der certo, recebe o JSON e faz o parse do pokémon com ID aleatório
    data = response.json()
    name = data["name"].capitalize()
    move = random.choice(data["moves"])["move"]["name"].replace("-", " ").title()

    # Se for o Charizard, ordena o array utilizando o sort built-in da linguagem Python
    if name != "Charizard":
        print(f"{name} usou {move}, mas não foi muito efetivo...\n")
        comparacoes["Charizard Sort"] += 1
        charizard_sort(arr)
    else:
        print(f"{name} usou {move}! Foi super efetivo!\n")
        arr.sort()
        comparacoes["Charizard Sort"] += len(arr) * math.log2(len(arr))
        return

# Função para testar os sorts, recebe função, nome, vetor e arquivo de output
def testar(sort_func, nome, vetor, output):
    vetor_copia = vetor.copy()
    comparacoes[nome] = 0
    inicio = time.perf_counter()
    if nome == "Quick Sort":
        sort_func(vetor_copia, 0, len(vetor_copia) - 1)
    else:
        sort_func(vetor_copia)
    fim = time.perf_counter()
    duracao_ms = (fim - inicio) * 1000

    output.write(f"{nome:<15} | Vetor: {', '.join(map(str, vetor_copia))} | Tempo: {duracao_ms:>10.3f} ms | Comparações: {int(comparacoes[nome])}\n")

# Função para criar vetores de acordo com especificação do enunciado
def criar_vetor(tam_vetor, char_ordem):
    if char_ordem == 'c':
        return list(range(1, tam_vetor + 1))
    elif char_ordem == 'd':
        return list(range(tam_vetor, 0, -1))
    elif char_ordem == 'r':
        return [random.randint(0, tam_vetor) for _ in range(tam_vetor)]

if __name__ == '__main__':

    # Checa número de argumentos
    if len(sys.argv) < 3:
        print("Uso: python script.py <arquivo_input.txt> <arquivo_output.txt> ")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]
    tam_vetor = 0
    char_ordem = ''

    # Checa extensão dos inputs
    if not input.endswith(".txt") or not output.endswith(".txt"):
        print("Argumentos devem ser do formato .txt")
        sys.exit(1)

    # Tenta abrir o arquivo de input para lê-lo
    try:
        with open(input, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f.readlines()]
            if len(linhas) != 2:
                print("Número inválido de linhas no arquivo de input")
                sys.exit(1)
            else:
                if linhas[0].isdigit() and (linhas[1] in ['c', 'd', 'r']):
                    tam_vetor = math.floor(int(linhas[0]))
                    char_ordem = linhas[1]
                else:
                    print("Arquivo em formato inválido")
                    sys.exit(1)
    except FileNotFoundError:
        print("Arquivo de input não encontrado")
        sys.exit(1)

    vetor = criar_vetor(tam_vetor, char_ordem)

    # Abre o arquivo de output, passa como argumento para função testar e testa todos os sorts
    with open(output, 'w', encoding='utf-8') as f:
        testar(bubble_sort, "Bubble Sort", vetor, f)
        testar(selection_sort, "Selection Sort", vetor, f)
        testar(insertion_sort, "Insertion Sort", vetor, f)
        testar(heap_sort, "Heap Sort", vetor, f)
        testar(quicksort_iterativo, "Quick Sort", vetor, f)
        testar(charizard_sort, "Charizard Sort", vetor, f)