class Heroi:

    def __init__(
        self,
        campos
    ):
        ( self.__key,
        self.__name,
        self.__alignment,
        self.__gender,
        self.__eye_color, 
        self.__race,
        self.__hair_color,
        self.__publisher,
        self.__skin_color,
        self.__height,
        self.__weight,
        self.__intelligence,
        self.__strength,
        self.__speed,
        self.__durability,
        self.__power,
        self.__combat,
        self.__total, ) = campos
    
    def get_key(self):
        return self.__key

    def print_heroi(self):
        for value in self.__dict__.items():
            print(f"{value}")


def parse_arquivo(arquivo, metodo, ordem):

    with open(arquivo, 'r', encoding='utf-8') as f:
        temp_lista = f.readlines()

    metodo = temp_lista.pop(0).strip().split(',')
    print(metodo[0][len(metodo[0]) - 1])

def main():
    
    metodo = 0
    ordem = 'C'
    parse_arquivo('input01.txt', metodo, ordem)

if __name__ == '__main__':
    main()