
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" +  tipo_pesos  + "tienes?: ")

    pesos = float(pesos)

    dolares = pesos / valor_dolar

    dolares = round(dolares, 2)

    dolares = str(dolares)

    print("Tienes $" + dolares + " dolares")
    




menu = """
Bienvenido al conversor de monedas!

1- Pesos colombianos
2- Pesos mexicanos
3- Pesos argentinos

Elige una opcion: """

opcion = input(menu)




if opcion == 1:

    conversor("colombianos", 3875)

elif opcion == 2:

    conversor("mexicanos", 20)

elif opcion == 3:

   conversor("argentinos", 60)

else: 
    print('Ingresa una opcion correcta')















