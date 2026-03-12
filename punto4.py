print ("escribir solo numero enteros:")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
d = int(input("Ingrese el cuarto número: "))
mayor = a

if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
if d > mayor:
    mayor = d

print("El número mayor es:", mayor)
