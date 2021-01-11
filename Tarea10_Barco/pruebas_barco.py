from barco import BoundedPriorityQueue

print("Prueba de colas con prioridad acotada")
maestres = {"prioridad":4, "descripcion":"Maestre", "personas": ["Juan P", "Diego H"]}
niños = {"prioridad":2, "descripcion":"Niños", "personas": ["Santi H", "Angel H"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos", "personas": ["Diana P", "Maria Z"]}
niñas = {"prioridad":1, "descripcion":"Niñas", "personas": ["Ana Z", "Daniela F"]}
adultos_mayores = {"prioridad":2, "descripcion":"Adultos Mayores", "personas": ["Ricardo H", "Felipe H"]}
hombres = {"prioridad":3, "descripcion":"Hombres", "personas": ["Saul Z", "Derek F"]}
mujeres = {"prioridad":3, "descripcion":"Mujeres", "personas": ["Sofia Z", "Fernanda F"]}
vigias = {"prioridad":4, "descripcion":"Vigias", "personas": ["Eric Z", "Fernando F"]}
capitan = {"prioridad":5, "descripcion":"Capitan", "personas": ["Felipe G"]}
timonel = {"prioridad":4, "descripcion":"Timonel", "personas": ["Alberto L", "Armando H"]}

bar = BoundedPriorityQueue(6)
bar.enqueue(maestres['prioridad'], maestres)
bar.enqueue(niños['prioridad'], niños)
bar.enqueue(mecanicos['prioridad'], mecanicos)
bar.enqueue(niñas['prioridad'], niñas)
bar.enqueue(adultos_mayores['prioridad'], adultos_mayores)
bar.enqueue(hombres['prioridad'], hombres)
bar.enqueue(mujeres['prioridad'], mujeres)
bar.enqueue(vigias['prioridad'], vigias)
bar.enqueue(capitan['prioridad'], capitan)
bar.enqueue(timonel['prioridad'], timonel)
bar.to_string()

print("Comienzo del desembarque")

m = 0
while not bar.is_empty():
    if (m < 6):
        bar.dequeue()
        bar.to_string()
        m+1
    else:
        print("Nivel vacio")
else:
    print("El barco fue abandonado con exito")
    
