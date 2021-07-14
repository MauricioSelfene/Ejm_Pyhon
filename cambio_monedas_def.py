def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos)
    #valor_dolar = 748
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 💰

1.- Pesos Chilenos
2.- Pesos Argentinos.
3.- Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Chilenos", 748)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Debes ingresar una opción valida")
