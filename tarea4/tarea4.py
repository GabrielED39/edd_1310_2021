from arrays import Array
class trabajador(Array):
    def horase (self,suelb,ext):
        return int(suelb) + (276.5 * init(ext))

    def prestaciones(self,anoin,sueldo);
    antigue = 2020 - ini(anoin)
    presta = int(sueldo)*((3*antigue)/100)
archivo = open('junio.dat')
archivo.readline()
empleados = trabajador(14)
for empleado in range(empleados.get_lenght()):
    datos = archivo.readline().split(',')
    empleados.set_item(datos,empleado)
#Horas extra
for empleado in empleados:
    newsuel = empleados.horase(empleado[5], empleado[4])
    empleado[5]=newsuel
#Prestaciones
for empleado in empleados:
    empleado[5] = int(empleado[5])+empleados.prestaciones(empleado[6][0:4],empleado[5])
for empleado in empleados:
    print(empleado)
#Antuguedad
for x in range(empleados.get_length()):
    for m in range(empleados.get_length()-1):
        if empleados.get_item(y)[6][0:14] > empleados.get_item(m+1)[6][0:4]:
            burbuja = empleados.get_item(m)
            'empleados[m] = empleados[y+1]'
            empleados.set_item(empleados.get_item(m+1),m)
            'empleados[m+1] = burbuja'
            empleados.set_item(burbuja,m+1)
            print(empleados)
