class Queue:
    def __init__(self):
        self.__data = list()
        
    def is_empty(self):
        return len(self.__data) == 0
    
    def length(self):
        return len(self.__data)
    
    def enqueue (self,elem):
        self.__data.append(elem)
        
    def dequeue (self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None
        
    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str(elem)
        cadena = cadena +"|"
        return cadena
    
    
#PRIORITY QUEUE
class PriorityQueue:
    def __init__(self):
        self.__data = list()
        
    def is_empty(self):
        return len(self.__data) == 0
    
    def enqueue (self,elem):
        self.__data.append(elem)
    
    def dequeue (self):
        try: 
            max = 0
            for x in range(len(self.__data)): 
                if self.__data[x] > self.__data[max]: 
                    max = x 
            item = self.__data[max] 
            del self.__data[max] 
            return item 
        except IndexError: 
            print() 
            exit() 
 
    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str(elem)
        cadena = cadena +"|"
        return cadena
        
    
class BoundedPriorityQueue:
    def __init__(self,niveles):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0
        
    def is_empty(self):
        return self.__size == 0
    
    def length(self):
        return self.__size
    
    def enqueue(self, prioridad, elem):
        if prioridad < len(self.__data) and prioridad >= 0:
            self.__data[prioridad].enqueue(elem)
            self.__size += 1
    
    def dequeue(self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size -= 1
                    return nivel.dequeue()
                
    def to_string(self):
        for nivel in range(len(self.__data)):
            print(f"Nivel {nivel} --> { self.__data[nivel].to_string() }")
            