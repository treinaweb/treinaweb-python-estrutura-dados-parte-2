from listas import lista_ligada

class Conjunto():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def inserir(self, elemento):
        pass

    def inserir_posicao(self, posicao, elemento):
        pass

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    def indice(self, elemento):
        return self.__elementos.indice(elemento)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def recuperar_elemento_no(self, posicao):
        return self.__elementos.recuperar_elemento_no(posicao)

    def recuperar_no(self, posicao):
        return self.__elementos.recuperar_no(posicao)

    def tamanho(self):
        return self.__elementos.tamanho

    def remover_posicao(self, posicao):
        self.__elementos.remover_posicao(posicao)

    def remover_elemento(self, elemento):
        self.__elementos.remover_elemento(elemento)