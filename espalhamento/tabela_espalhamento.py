from listas import lista_ligada

class TabelaEspalhamento():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())




# 0 (0, 50):
# 1 (50,100):
# 2 (100,150):
# 3 (150:200):