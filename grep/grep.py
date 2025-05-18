import sys

def grep(arquivo, string):

    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            if string in linha:
                linha = linha.replace(string, f'\033[31m{string}\033[0m')
                print(linha)

def grep_novo(arquivo, string):

    with open(arquivo, 'r', encoding='utf-8') as f:
        i = 0
        for linha in f:
            i += 1
            if string in linha:
                linha = linha.replace(string, f'\033[31m{string}\033[0m')
                print(f'[\033[31m{i:>3}\033[0m ] | {linha}')

def read_record_by_rrn(arquivo, rrn):

    if rrn < 0:
        print("RRN inválido, informe um valor maior que 0")
        sys.exit(1)

    with open(arquivo, 'r', encoding='utf-8') as f:

        i = 0
        for linha in f:
            if i == rrn:
                linha = linha.replace(linha, f'\033[31m{linha}\033[0m')
                print(linha)
                return
            i += 1

        if i < rrn:
            print("Registro não encontrado")
            sys.exit(1)
   
                
if __name__ == '__main__':

    

    input = sys.argv[1]

    if sys.argv[2].isdigit():
        rrn = int(sys.argv[2])
        read_record_by_rrn(input, rrn)
    else:
        target = sys.argv[2]
        grep(input, target)
        grep_novo(input, target)