from Model.ArbolBinario import ArbolBinario
class Controller:
    def __init__(self):
        print("Funciona controller")
        arbol = ArbolBinario("F")
        arbol.agregar("A")
        arbol.agregar("B")
        arbol.agregar("C")
        arbol.agregar("D")
        arbol.agregar("E")
        arbol.agregar("G")
        arbol.agregar("H")
        arbol.agregar("I")
        decision = int(0)
        while decision == 0:
            decision1 = int(input("Arboles Binarios\n1. Agregar valor\n2. Recorrido post-orden"
                                  "\n3. Recorrido pre-orden\n4. Recorrido in-orden\n5. Salir: "))
            if decision1 == 1:
                valor = str(input("Ingrese el valor a insertar: "))
                arbol.agregar(valor)
                print("Valor agregado correctamente")
            elif decision1 == 2:
                arbol.postOrden()
            elif decision1 == 3:
                arbol.preOrden()
            elif decision1 == 4:
                arbol.inOrden()
            elif decision1 == 5:
                decision+=1








