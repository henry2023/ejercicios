t = int(input("Ingresar Total de Horas: "))
print("Semanas: ", t/(24*7))
print("Dias: ", t%(24*7)/24)
print("Horas: ", t%24)