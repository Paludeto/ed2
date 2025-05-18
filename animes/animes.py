# Devolve o input formatado em formato de lista
def lista_formatada(arquivo):

    lista = []

    # Deixa no formato adequado, sem newline, com pipes no lugar das vírgulas e sem o header
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            lista.append(linha.strip().replace(',', '|'))
    lista.pop(0)

    return lista

# Escrita para registros fixos, campos de tamanho variável
def escrita_reg_fixo(arquivo, lista):

    # Pega item com o maior tamanho
    maior_tam = max(len(linha) for linha in lista)

    with open('output_reg_fixo.txt', 'w', encoding='utf-8') as f:
        for linha in lista:
            padding = maior_tam - len(linha)
            f.write(linha + (padding * '*') + '\n')

# Simplesmente remove o '\n'
def escrita_campo_fixo(arquivo, lista):

    with open('output_campo_fixo.txt', 'w', encoding='utf-8') as f:
        for linha in lista:
            f.write(linha + '|')

# Prepend no número de bytes
def escrita_qtde_bytes(arquivo, lista):

    with open('output_qtde_bytes.txt', 'w', encoding='utf-8') as f:
        for linha in lista:
            f.write(str(len(linha)) + linha + '|')

# Apenas escreve o tamanho de cada entrada
def escrita_arq_indice(arquivo, lista):

    with open('output_arq_indice.txt', 'w', encoding='utf-8') as f:
        for linha in lista:
            f.write(str(len(linha)) + ' ')

# Dá append em um delimitador no final da entrada
def escrita_delim(arquivo, lista):

    with open('output_delim.txt', 'w', encoding='utf-8') as f:
        for linha in lista:
            f.write(linha + '|#')
    
def gerar_outputs(arquivo):

    lista = lista_formatada(arquivo)

    escrita_reg_fixo(arquivo, lista)
    escrita_campo_fixo(arquivo, lista)
    escrita_qtde_bytes(arquivo, lista)
    escrita_arq_indice(arquivo, lista)
    escrita_delim(arquivo, lista) 

def main():

    gerar_outputs('animes.csv')

if __name__ == '__main__':

    main()