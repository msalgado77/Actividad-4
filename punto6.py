print("Este programa solo acepta números enteros")

octal = input("Ingrese un número octal de 5 dígitos: ")

if len(octal) == 5:
    decimal = int(octal, 8)
    print("El equivalente en decimal es:", decimal)
else:
    print("Debe ingresar exactamente 5 dígitos.")