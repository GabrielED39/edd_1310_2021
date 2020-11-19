class Nodo:
    def __init__( self , value , siguiente= None):
        self.data = value   #Falta Encapsulamiento
        self.siguiente = siguiente

#Metodo head (crea el nodo cabeza)
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
        while cuur_node.siguiente != None: #Pregunta si curr_node es diferente a vacio(si ya estamos en el final o no)
            curr_node = curr_node.siguiente
        curr_node.siguiente = nuevo
    def transversal (self):
        curr_node = self.__head
        while curr_node != None:
            print(f'{curr_node.data} ->',end="")
            curr_node = curr_node.siguiente
        print(" ")

#Metodo tail
def tail(self):
    curr_node = self.__head
    while curr_node.siguiente != None:
        curr_node = curr_node.siguiente
    return curr_node

#Metodo remove (Elimina un nodo)
def remove(self, value):
    curr_node = self.__head
    if self.__head.data == value: # Este if cambia de nodo si se esta eliminando head
        self.__head = self.__head.siguiente
    else:
        anterior = None
        while curr_node.data != value and curr_node.siguiente != None:
            anterior = curr_node #con esto se almacena el nodo anterior
            curr_node = curr_node.siguiente
        if curr_node.data == value:
            anterior.siguiente = curr_node.siguiente
        else:
            print("El dato no existe en la lista")

#Metodo preppend (Agrega un nuevo nodo al principio)
def preppend(self,value):
    nuevo = Nodo(value, self.__head) #Crea el nuevo nodo
    self.__head = nuevo #Le da al nuevo nodo el valor de head

def get(self,posicion = None): #Por defecto regresa el ultimo
    contador = 0
    dato = None
    if posicion = None:
        dato = self.tail().data #Esto se convierte en un Nodo
    else:
        pass

    return dato
