""" Sorprendentemente, solo hay tres números que se pueden escribir como la suma de los cuartos potencias de sus dígitos:

1634 = 1 4 + 6 4 + 3 4 + 4 4
8208 = 8 4 + 2 4 + 0 4 + 8 4
9474 = 9 4 + 4 4 + 7 4 + 4 4
Como 1 = 1 4 no es una suma, no se incluye.

La suma de estos números es 1634 + 8208 + 9474 = 19316.

Encuentra la suma de todos los números que se pueden escribir como la suma de quintas potencias de sus dígitos. """
numero =0
suma =0
for i in range(295245):
    numero = str(i)
    digitos = [0,0,0,0,0,0]
    longitud = len(numero)
    for x in range(longitud):
        digitos[x]=numero[x]
    poder = int(digitos[0])**5+int(digitos[1])**5+int(digitos[2])**5+int(digitos[3])**5+int(digitos[4])**5+int(digitos[5])**5
    if numero == str(poder) and int(numero) > 1:
        print('Numero del poder: '+str(numero))
        suma += int(poder)
print('Suma del poder: '+str(suma))

# RESUELTO 16/06/2021


""" 
NO SABIA COMO OBTENER EL LIMITE SUPERIOR ASI QUE PUSE UN NUMERO AL AZAR 999999 PERO EN REALIDAD AQUI ESTA LA RESPUESTA
Lo admito, utilicé el desbordamiento de pila para que la función separara los números en dígitos individuales. No estaba seguro de cómo hacer eso. el resto fue simple. 2 ** 5 es 64 y 9 ** 5 por 5 es 295245. Así que eso definió el límite superior. Luego revisé cada uno y los recogí."""
