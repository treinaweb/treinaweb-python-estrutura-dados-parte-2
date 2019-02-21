

#       R     -- Raiz
#     E    D  -- Nós
#         E D -- Folhas
#
#
#       10      -- Raiz
#     5   15   -- Nós
#           16 -- Folha
#

class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if(self.__raiz == None):
            self.__raiz = no
        else:
            if (self.__raiz.peso() > no.peso()):
                self.__raiz.no_esquerdo = no
            else:
                self.__raiz.no_direito = no


