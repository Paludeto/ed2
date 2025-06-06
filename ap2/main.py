# Aluno: Gabriel Paludeto 
# RA: 2605643
import heapq
import sys

# ===============================================================================================================================

class Heroi:

    # Coisa horrível esse construtor, deu até arrepio na nuca
    def __init__(self, campos):

        if len(campos) != 18:
            raise ValueError("Número de campos inválidos")

        self.__key = int(campos[0])
        self.__name = campos[1]
        self.__alignment = campos[2]
        self.__gender = campos[3]
        self.__eye_color = campos[4]
        self.__race = campos[5]
        self.__hair_color = campos[6]
        self.__publisher = campos[7]
        self.__skin_color = campos[8]
        self.__height = campos[9]
        self.__weight = campos[10]
        self.__intelligence = campos[11]
        self.__strength = campos[12]
        self.__speed = campos[13]
        self.__durability = campos[14]
        self.__power = campos[15]
        self.__combat = campos[16]
        self.__total = campos[17]

    def get_key(self):

        return self.__key
    
    # Meus olhos sangram
    def __str__(self):
        return '|'.join([
            str(self.__key),
            str(self.__name),
            str(self.__alignment),
            str(self.__gender),
            str(self.__eye_color),
            str(self.__race),
            str(self.__hair_color),
            str(self.__publisher),
            str(self.__skin_color),
            str(self.__height),
            str(self.__weight),
            str(self.__intelligence),
            str(self.__strength),
            str(self.__speed),
            str(self.__durability),
            str(self.__power),
            str(self.__combat),
            str(self.__total)
        ])

# ===============================================================================================================================

# Função auxiliar
def comparar(a, b, reverso):

    return a > b if reverso else a < b

# Quick
def quick_sort(arr, reverso=False):

    if len(arr) <= 1:
        return arr[:]
    pivo = arr[0].get_key()
    menores = [x for x in arr[1:] if comparar(x.get_key(), pivo, not reverso)]
    maiores = [x for x in arr[1:] if comparar(x.get_key(), pivo, reverso)]
    return quick_sort(menores, reverso) + [arr[0]] + quick_sort(maiores, reverso)

# Heap
def heap_sort(arr, reverso=False):

    copia = [(h.get_key(), h) for h in arr]
    if reverso:
        copia = [(-int(k), h) for k, h in copia]  # cast para int pra poder inverter com -
    else:
        copia = [(int(k), h) for k, h in copia]
    heapq.heapify(copia)
    return [heapq.heappop(copia)[1] for _ in range(len(copia))]

# Merge
def merge_sort(arr, reverso=False):

    if len(arr) <= 1:
        return arr[:]
    meio = len(arr) // 2
    esq = merge_sort(arr[:meio], reverso)
    dir = merge_sort(arr[meio:], reverso)
    return merge(esq, dir, reverso)

def merge(esq, dir, reverso):

    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if comparar(esq[i].get_key(), dir[j].get_key(), not reverso):
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

# Insertion
def insertion_sort(arr, reverso=False):

    resultado = arr[:]
    for i in range(1, len(resultado)):
        chave = resultado[i]
        j = i - 1
        while j >= 0 and comparar(chave.get_key(), resultado[j].get_key(), reverso):
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = chave
    return resultado

# ===============================================================================================================================

def parse_arquivo(arquivo):

    with open(arquivo, 'r', encoding='utf-8') as f:
        temp_lista = f.readlines()

    # Primeiro pop pra extrair metadados
    header = temp_lista.pop(0).strip().split(',')

    metodo_sort = header[0].split('=')[1]
    ordem_sort = header[1].split('=')[1]

    # Segundo pop pra mandar o cabeçalho pra casa do chapéu
    temp_lista.pop(0)

    lista_heroi = []

    for linhas in temp_lista:
        campos = linhas.strip().split('|')
        lista_heroi.append(Heroi(campos))

    # Esse return triplo foi a coisa mais horrenda que eu já fiz em 4 anos de programação
    return lista_heroi, metodo_sort, ordem_sort

def keysort_herois(lista, metodo_sort, ordem_sort):

    # Switch-case nessa linguagem maldita é uma feature nova (3.10). Não vou me arriscar.
    if ordem_sort == 'C':
        crescente = True
    elif ordem_sort == 'D':
        crescente = False
    else:
        raise ValueError("Ordem inválida!")

    if metodo_sort == 'Q':
        return quick_sort(lista, crescente)
    elif metodo_sort == 'H':
        return heap_sort(lista, crescente)
    elif metodo_sort == 'M':
        return merge_sort(lista, crescente)
    elif metodo_sort == 'I':
        return insertion_sort(lista, crescente)
    else:
        raise ValueError("Método inválido!")
    
def escreve_arquivo(lista_herois, output):

    with open(output, 'w', encoding='utf-8') as f:

        # hardcoded mesmo, pra passar no teste do script
        f.write("key,Name,Alignment,Gender,EyeColor,Race,HairColor,Publisher,SkinColor,Height,Weight,Intelligence,Strength,Speed,Durability,Power,Combat,Total\n")
        for heroi in lista_herois:
            f.write(str(heroi) + '\n')

def main():

    if len(sys.argv) < 3:
        print("Uso: python script.py <arquivo_input.txt> <arquivo_output.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not input_file.endswith(".txt") or not output_file.endswith(".txt"):
        print("Argumentos devem ser do formato .txt")
        sys.exit(1)

    
    # Exception handling em caso de absurdidades
    try:
        lista_herois, metodo_sort, ordem_sort = parse_arquivo(input_file) 
        lista_herois = keysort_herois(lista_herois, metodo_sort, ordem_sort)
    except ValueError:
        print("Alguma coisa de errada não está certa nos seus metadados. Faça o L imediatamente.")
        exit()

    escreve_arquivo(lista_herois, output_file)


if __name__ == '__main__':

    main()