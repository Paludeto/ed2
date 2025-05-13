import time

# ═══════════════════════════════════════════🫧 BUBBLE SORT 🫧══════════════════════════════════════════════════

def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ═══════════════════════════════════════════🔎 SELECTION SORT 🔎═══════════════════════════════════════════════

def selection_sort(arr):

    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# ═══════════════════════════════════════════📌 INSERTION SORT 📌═══════════════════════════════════════════════

def insertion_sort(arr):

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# ═══════════════════════════════════════════🔥 HEAP SORT 🔥══════════════════════════════════════════════════

def heapify(arr, n, i):

    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
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

# ═══════════════════════════════════════════⚡ QUICK SORT ⚡══════════════════════════════════════════════════

def quicksort(arr, inicio=0, fim=None):

    if fim is None:
        fim = len(arr) - 1
    if inicio < fim:
        p = particiona(arr, inicio, fim)
        quicksort(arr, inicio, p - 1)
        quicksort(arr, p + 1, fim)

def particiona(arr, inicio, fim):

    pivo = arr[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

# ═══════════════════════════════════════════🧪 TESTES DE TEMPO 🧪═══════════════════════════════════════════════

def testar(sort_func, nome):
    
    vetor = [-93, 97, -92, 69, -7, 6, 94, 53, 35, -34, 0, -14, -26, 32, 87]
    vetor_copia = vetor.copy()

    inicio = time.perf_counter()
    if nome == "Quick Sort":
        sort_func(vetor_copia, 0, len(vetor_copia) - 1)
    else:
        sort_func(vetor_copia)
    fim = time.perf_counter()

    duracao_ms = fim - inicio
    print(f"{nome:<15}: {vetor_copia}")
    print(f"Tempo: {duracao_ms:.3e} ms\n")

testar(bubble_sort, "Bubble Sort")
testar(selection_sort, "Selection Sort")
testar(insertion_sort, "Insertion Sort")
testar(heap_sort, "Heap Sort")
testar(quicksort, "Quick Sort")