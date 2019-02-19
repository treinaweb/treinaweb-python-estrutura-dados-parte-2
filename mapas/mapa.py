from listas import lista_ligada

# 0: ("par", 10)
# 1: 15, 25, 35,
# 2: 16, 26, 36
# 3 (150:200):

class Mapa():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numero_categorias = 10

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())

    def gerar_numero_espalhemnto(self, chave):
        return hash(chave) % self.__numero_categorias