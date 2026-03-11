manzanas = int(input("Hola, por favor ingrese cuántas manzanas compró el cliente: "))

if manzanas <= 2:
    respuesta = input("Tendrás un 0% de descuento, ¿Quieres saber cuánto debe pagar el cliente? (Sí/No): ")
    if respuesta.lower() == "si":
        precio_manzana = int(input("Por favor digite el precio unitario de la manzana: "))
        total = manzanas * precio_manzana
    else:
        print("Oh bueno, te deseo suerte al hacer el cálculo")
        exit()

elif manzanas >= 3 and manzanas <= 5:
    respuesta = input("Tendrás un 10% de descuento, ¿Quieres saber cuánto debe pagar el cliente? (Sí/No): ")
    if respuesta.lower() == "si":
        precio_manzana = int(input("Por favor digite el precio unitario de la manzana: "))
        total = manzanas * precio_manzana * (1 - 0.10)
    else:
        print("Oh bueno, te deseo suerte al hacer el cálculo")
        exit()

elif manzanas >= 6 and manzanas <= 10:
    respuesta = input("Tendrás un 15% de descuento, ¿Quieres saber cuánto debe pagar el cliente? (Sí/No): ")
    if respuesta.lower() == "si":
        precio_manzana = int(input("Por favor digite el precio unitario de la manzana: "))
        total = manzanas * precio_manzana * (1 - 0.15)
    else:
        print("Oh bueno, te deseo suerte al hacer el cálculo")
        exit()

else:
    respuesta = input("Tendrás un 20% de descuento, ¿Quieres saber cuánto debe pagar el cliente? (Sí/No): ")
    if respuesta.lower() == "si":
        precio_manzana = int(input("Por favor digite el precio unitario de la manzana: "))
        total = manzanas * precio_manzana * (1 - 0.20)
    else:
        print("Oh bueno, te deseo suerte al hacer el cálculo")
        exit()

print("El valor que el cliente deberá pagar será de $", total)