class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right
        
arbol = NodoArbol("R",NodoArbol("C",None,None),NodoArbol("H")) 
#Los None en esta caso no van ya que por de fecto se toma el None sin necesidad de colocarlo
#Sin embargo no ocasiona nada ponerlos
print (arbol.left.data) #imprime el nodo izquierdo del arbol
print (arbol.right.data) #imprime el nodo derecho del arbol
print (arbol.data) #imprime la raiz del arbol

print("Arbol Dos")

arbol2 = NodoArbol(4, NodoArbol(3, NodoArbol(2, NodoArbol(2))), NodoArbol(5))
print(arbol2.data) #imprime raiz "4"
print(arbol2.left.data) #Imprime izquierda "3"
print(arbol2.left.left.data) #Imprime izquierda de izquierda "2"
print(arbol2.left.left.left.data) #Imprime izquierda de izquierda de izquierda "2"