no = []
ed = []
while True:	
	n = input("Nombre: ")
	if n != "*":
		no.append(n)
		ed.append(int(input("Edad: ")))
	if n == "*": break;	
edad_max = max(ed)
print("Mayores de edad")
for nombre,edad in zip(no,ed):
	if edad >= 18:
		print(nombre)
print("Alumnos mayores")
for nombre,edad in zip(no,ed):
	if edad == edad_max:
		print(nombre)