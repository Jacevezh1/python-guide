```Asignación de variables```

En Python, creamos las variables asignándoles un valor de la siguiente manera:
<identificador> = <valor>
en este caso el signo = se lee como “asignar”

Reasignación de variables
Podemos en cualquier momento cambiar el valor de nuestra variable volviendo a asignar un valor al mismo identificador:
<identificador> = <nuevo_valor>

Reglas en el uso de identificadores de variable
No pueden empezar con un número.
Deben estar en minúsculas
Para separar las palabras usamos el guion bajo: _
Estas reglas son aplicadas al lenguaje Python, en otros lenguajes puede haber otras reglas.
Tipos de variables en Python
a = 28 → int (entero)
b = 1.5 → float (decimales)
c = “Hello” → str (string o cadena de texto)
d = True → boolean (verdadero o falso)
e = None → NoneType (Sin valor)
f = “5” → str (5 y “5” no son lo mismo. La primera es un entero y la segunda una cadena de texto)








```Tipos de datos primitivos en Python```

Integers: números Enteros
Floats: números de punto flotante (decimales)
Strings: cadena de caracteres (texto)
Boolean: boolenaos (Verdadero o Falso)
Algunos operadores aritméticos pueden funcionar para operar con otros tipos de datos. Por ejemplo: podemos sumar strings, lo que concatena el texto o multiplicar un entero por un string, lo que repetirá el _string _las veces que indique el entero.

Tipos de dato adicionales
Datos en texto: str
Datos numéricos: int, float, complex
Datos en secuencia: list, tuple, range
Datos de mapeo: dict
Set Types: set, frozenset
Datos booleanos: bool
Datos binarios: bytes, bytearray, memoryview





```Cómo convertir un tipo de dato a otro en Python:```

Sintaxis Descripción

int(var) variable a entero
float(var) variable a flotante
str(var) variable a texto
bool(var)variable a booleano
abs(var) variable a valor absoluto






```Conoce los operadores lógicos que tiene Python y cómo utilizarlos de manera adecuada:```

Operadores lógicos
and ( y ): compara dos valores, y si ambos son verdaderos, devuelve True.
or ( ó ): si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo devuelve falso cuando los dos valores no se cumplen.
not ( no): invierte el valor de una variable, dando el valor contrario al de la variable evaluada.
Operadores de comparación
== ( igual qué ): determina si dos valores son iguales o no.
!= (diferente de): determina si dos valores son distintos o no. Si los valores son diferentes devuelve True, si son iguales devuelve False.
> (mayor que): compara dos valores, y determina si es mayor que el otro.
< (menor que): compara dos valores y determina si es menor que el otro.
>= (mayor o igual): compara dos valores y determinas si es mayor o igual que el otro.
<= (menor o igual): compara dos valores y determinas si es menor o igual que el otro.
