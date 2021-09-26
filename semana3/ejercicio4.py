lista = []
n = int(input("Introduce un número: "))
while n>=0:
	lista.append(n)
	n = int(input("Introduce un número: "))

for n in lista:
	print(n," ",end="")
