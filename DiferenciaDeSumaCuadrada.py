""" 
La suma de los cuadrados de los primeros diez números naturales es,

El cuadrado de la suma de los primeros diez números naturales es,

Por lo tanto, la diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es .

Calcula la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.
"""
suma = 0
cuadrada = 0
sumacuadrada = 0
for i in range(101):
    suma += i**2
    cuadrada += i
sumacuadrada = cuadrada**2
resultado =0
resultado = sumacuadrada-suma
print('la diferencia es: '+str(resultado))

# RESUELTO 16/06/2021