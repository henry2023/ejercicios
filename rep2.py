nombres = []
horas = []
sueldo = []
n = int(input("Nº de personas: "))
for i in range (n):
    nombre = input("Nombre: ")
    nombres.append(nombre)
    h = int(input("Hora: "))
    horas.append(h)
    s = h*30
    sueldo.append(s)
for i in range (0,n):
    print(nombres[i],"-",horas[i],"-",sueldo[i])