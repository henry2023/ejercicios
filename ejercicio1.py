import math 
a = int(input("Ingresar número para a : "))
b = int(input("Ingresar número para b : "))
c = float(input("Ingresar número para c : "))

x1 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
print(x1)
