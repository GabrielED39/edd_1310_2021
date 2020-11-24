# Crea la clase node
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#Crea la clase linked_list
class lista_doble:
    def __init__(self):
        self.head = None

    #Agregar elementos al frente de la lista
    def add_frente(self, data):
        self.head = node(data=data, next=self.head)

    #Comprueba si los datos son None
    def is_empty(self):
        return self.head == None

    #Agrega elementos al final de la lista
    def add_fin(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

    #Elemina nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    #Obtiene el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data
        
    #Imprime lista de nodos
    def imprimir_lista( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next

m = lista_doble() 
m.add_frente(25) 
m.add_fin(10) 
m.add_frente(20)
m.add_fin(5)
m.add_fin(12)
m.imprimir_lista() # Imprime lista de nodos
