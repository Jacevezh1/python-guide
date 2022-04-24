from xml.etree.ElementInclude import include


def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

    for i in range(10000):
        print(i)
        if i == 5000:
            break
        
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

    texto2 = input('Escribe un texto: ')
    while texto2.length > 4:
        print('Mayor que 4')  
        break     


if __name__ == '__main__':
    run()