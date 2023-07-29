""" 145 es un número curioso, ¡como 1! + 4! + 5! = 1 + 24 + 120 = 145.

Encuentra la suma de todos los números que son iguales a la suma del factorial de sus dígitos.

Nota: ¡Como 1! = 1 y 2! = 2 no son sumas no están incluidas. """

import math

sumacomparar = 0
sumatem=0
sumarespuesta=0
for i in range(3,362882):
    longitud = len(str(i))
    numero = str(i)
    sumacomparar=0
    for x in range(longitud):
        sumacomparar += math.factorial(int(numero[x]))
    if(sumacomparar == i):
        sumarespuesta+=sumacomparar

print("La suma es: "+str(sumarespuesta))

# RESUELTO 21/06/2021 11:24am
