notas = []
for indice in range(1,5):
	while True:
		nota = int(input("Introduce nota: " ))
		if nota>=0 and nota<=10: break
	notas.append(nota)

print("Notas: ",end="")
for nota in notas:
	print(nota," ",end="")
print()
print("Nota media: ",sum(notas)/len(notas))
print("Nota alta: ",max(notas))
print("Nota menor: ",min(notas))
