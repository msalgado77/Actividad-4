print("Este programa suma el menor y el mayor de 4 números enteros")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
d = int(input("Ingrese el cuarto número: "))

numeros = [a, b, c, d]

menor = min(numeros)
mayor = max(numeros)

suma = menor + mayor

print("El número menor es:", menor)
print("El número mayor es:", mayor)
print("La suma del menor y mayor es:", suma)
