def remove_registro(arquivo, chave):

    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(arquivo, 'w', encoding='utf-8') as f:
        found = False
        for line in linhas:
            nome = line.strip().split('|')[0]  # usando nome como key
            if chave == nome:
                novo_nome = nome.replace(nome[0:2], "*|")
                line = line.replace(nome, novo_nome)
                found = True
                print("Registro nukado ☢️")
            f.write(line)
        if found == False:
            print("Chave não encontrada!")

def compactacao_arquivo(arquivo):

    with open(arquivo, 'r', encoding='utf-8') as f:

        linhas = f.readlines()

    linhas = [linha for linha in linhas if not linha.startswith("*|")]

    with open(arquivo, 'w', encoding='utf-8') as f:

        f.writelines(linhas)
    
if __name__ == '__main__':
    
    remove_registro('dataset.txt', 'Naruto Shippuuden')
    remove_registro('dataset.txt', 'Shugo Chara')
    compactacao_arquivo('dataset.txt')