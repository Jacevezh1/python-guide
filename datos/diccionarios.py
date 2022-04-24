# Estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden.
# Identifican cada elemento por una clave (Key) {}


def run():
    mi_diccionario = {
        'Llave1': 1,
        'Llave2': 2,
        'Llave3': 3
    }
    #print(mi_diccionario)
    #print(mi_diccionario['Llave1'])
    #print(mi_diccionario['Llave2'])
    #print(mi_diccionario['Llave3'])

    poblacion_paises = {
        'Arg': 120000,
        'Bra': 20000,
        'Mex': 10000
    }

    #Imprimir llaves de mi diccionario
    for pais in poblacion_paises.keys():
        print(pais)

    #Imprimir valores de mi diccionario
    for pais in poblacion_paises.values():
        print(pais)


if __name__ == '__main__':
    run()