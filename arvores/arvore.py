

#       R     -- Raiz
#     E    D  -- Nós
#         E D -- Folhas
#
#
#       10      -- Raiz
#     5   15   -- Nós
#           16 -- Folha
# X 5 X 10 X 15 X 16 X

class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    # 9
    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if(self.__raiz == None):
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)

    #   9
    #   7
    #       10
    #    9     12
    def __inserir(self, referencia, novo_no):
        if referencia.peso() < novo_no.peso():
            if referencia.no_direito == None:
                referencia.no_direito = novo_no
            else:
                self.__inserir(referencia.no_direito, novo_no)
        else:
            if referencia.no_esquerdo == None:
                referencia.no_esquerdo = novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)


    def __str__(self):
        return "[(X)]" if self.__raiz == None else self.__raiz.__str__()
