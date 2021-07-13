#Conversor de modenas v1

#Dolar a peso chileno
pesos = input("Cuantos pesos tienes? ")
pesos = float(pesos)
valor_dolar = 748
dolares = pesos / valor_dolar
dolares = round(dolares, 2)

dolares = str(dolares)

print("Tienes $" + dolares + " dolares")
print("--------------------------------")



#Peso Chileno a Dolar
dolar = input("Cuantos dolares tienes ?")
dolar = float(dolar)
valor_peso = 0.0013
pesos_dolar =  dolar / valor_peso
pesos_dolar = round(pesos_dolar, 2)

pesos_dolar = str(pesos_dolar)

print("Tienes $" + pesos_dolar + " pesos Chileno")
print("--------------------------------")