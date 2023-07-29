"""Comenzando con el número 1 y moviéndose hacia la derecha en el sentido de las agujas del reloj, se forma una espiral de 5 por 5 de la siguiente manera:

21 22 23 24 25
20 07 08 09 10
19 06 01 02 11
18 05 04 03 12
17 16 15 14 13

Se puede verificar que la suma de los números de las diagonales es 101.

¿Cuál es la suma de los números en las diagonales en una espiral de 1001 por 1001 formada de la misma manera?"""
anteriorr = [1,1,1,1]
iniciales = [8,2,4,6]
siguiente = [0,0,0,0]
suma = 0
for i in range(500):
    #09
    siguiente[0] = anteriorr[0]+(8*i)+iniciales[0]
    anteriorr[0]=siguiente[0]
    #print(siguiente[0])
    # 03
    siguiente[1] = anteriorr[1]+(8*i)+iniciales[1]
    anteriorr[1] = siguiente[1]
    #print(siguiente[1])
    # 05
    siguiente[2] = anteriorr[2]+(8*i)+iniciales[2]
    anteriorr[2] = siguiente[2]
    #print(siguiente[2])
    # 07
    siguiente[3] = anteriorr[3]+(8*i)+iniciales[3]
    anteriorr[3] = siguiente[3]
    #print(siguiente[3])
    # sumas las diagonales del nivel
    suma += siguiente[0]+siguiente[1]+siguiente[2]+siguiente[3]
suma +=1

print("suma: "+str(suma))

# RESUELTO 21/06/2021 12:49 PM
