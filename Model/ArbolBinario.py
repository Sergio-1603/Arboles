from Model.Nodo import Nodo
class ArbolBinario:
    raiz = None

    def __init__(self, r):
        self.raiz = Nodo(r)

    def __agregarValor(self, nodo, dato):
        if dato<nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregarValor(nodo.izquierda,dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)

            else:
                self.__agregarValor(nodo.derecha,dato)

    def __inOrden(self,nodo):
        if nodo is not None:
            self.__inOrden(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inOrden(nodo.derecha)

    def __postOrden(self, nodo):
        if nodo is not None:
            self.__postOrden(nodo.izquierda)
            self.__postOrden(nodo.derecha)
            print(nodo.dato, end=", ")
    def __preOrden(self,nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preOrden(nodo.izquierda)
            self.__preOrden(nodo.derecha)

    def postOrden(self):
        print("Recorrido post-orden")
        self.__postOrden(self.raiz)
        print("")

    def inOrden(self):
        print("Recorrido in-orden")
        self.__inOrden(self.raiz)
        print("")

    def preOrden(self):
        print("Recorrido pre-orden")
        self.__preOrden(self.raiz)

    def agregar(self,dato):
        self.__agregarValor(self.raiz,dato)

