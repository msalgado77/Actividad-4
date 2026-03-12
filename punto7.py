escritorios = int(input("Hola, por favor ingrese cuántos escritorios compró el cliente: "))
precio_escritorio = 800000

if escritorios < 5:
    total = escritorios * precio_escritorio * (1 - 0.10)
elif escritorios >= 5 and escritorios < 10:
    total = escritorios * precio_escritorio * (1 - 0.20)
else:
    total = escritorios * precio_escritorio * (1 - 0.40)

print("El valor que se le cobrará al cliente será $", total)

