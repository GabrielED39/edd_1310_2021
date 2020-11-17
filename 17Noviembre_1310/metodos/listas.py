class Nodo:
    def __init__( self , value , siguiente= None):
        self.data = value   #Falta Encapsulamiento
        self.siguiente = siguiente

#Metodo head
class LinkedList:
    def __init__( self ):
        self.__head = None

#Metodo empty
    def is_empty(self):
        return self.__head == None

#Metodo append
def append(self, value):
    nuevo = Nodo(value)
    if self.__head == None: #self.is_empty() (se puede sustituir)
        self.__head = nuevo
    else:
        curr_node =  head
        while cuur_node.siguiente != None:
            curr_node = curr_node.siguiente
        curr_node.siguiente = nuevo
    def transversal (self):
        curr_node = self.__head
        while curr_node != None:
            print(f'{curr_node.data} ->',end="")
            curr_node = curr_node.siguiente
        print("")
