from listas import LinkedList

l = LinkedList()
print(f'L está vacía? { l.is_empty()}')
l.append(10) #Apunta a 5
l.append(5) #Apunta a 6
l.append(6) #Apunta a 20
l.append(20) #Apunta a None
print(f'L está vacía? { l.is_empty()}')
l.transversal()
l.remove(10)
l.transversal()
l.preppend(3)
l.transversal()
x = l.tail()
print(x.data)
print(l.get())
