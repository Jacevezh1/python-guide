import random 


def run():
    numero_aletorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    vidas = 5
    while numero_elegido != numero_aletorio:
        if numero_elegido < numero_aletorio:
            print('Busca un numero mas grande')
            vidas -= 1
        elif numero_elegido > numero_aletorio:
            print('Elige un numero mas pequeno') 
            vidas -= 1
        if vidas == 0:
            print('Game over')
            break
        print('Tienes', vidas, "vidas")
        numero_elegido = int(input('Elige otro numero: '))
        if numero_elegido == numero_aletorio:
            print('Ganaste')
            break







if __name__ == '__main__':
    run()



