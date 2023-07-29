"""
PROBLEMA 5
2520 es el número más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin ningún resto.

¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?
"""
fin =False
i = 2
while fin == False:
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        print(i)
        fin = True
    i+=1

# RESUELTO 03/08/2021 18:55
