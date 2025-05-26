def remove_registro(arquivo, chave):

    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    header = int(linhas[0].replace('\n', '').split(':')[1])
    print(f"Topo da pilha antes: {header}")

    found = False

    for i in range(1, len(linhas)):
        nome = linhas[i].strip().split('|')[0]

        if chave == nome:
            found = True

            linhas[i] = f"*|{header}|{'|'.join(linhas[i].strip().split('|')[1:])}"
            tam = 424 - len(linhas[i])
            linhas[i] = linhas[i] + tam * '*' + '\n'
            print("Registro nukado ☢️")

            header = i - 1
            break

    if found:
        linhas[0] = f"head:{header}\n"
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.writelines(linhas)
    else:
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
    # compactacao_arquivo('dataset.txt')