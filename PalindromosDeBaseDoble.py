# Problema 36
# El número decimal, 585 = 1001001001 2 (binario), es palindrómico en ambas bases.
#
# Encuentre la suma de todos los números, menos de un millón, que son palindrómicos en base 10 # y base 2.
#
# (Tenga en cuenta que el número palindrómico, en cualquier base, puede no incluir ceros a la # izquierda).
#1000000
suma = 0
for i in range(999999):
    nbase10 = [0, 0, 0, 0, 0, 0, 0]
    nbase10alrevez = [0, 0, 0, 0, 0, 0, 0]
    cadena = "       "
    lon = len(str(i))
    cadena = str(i)
    for x in range(lon):
        nbase10[x]=cadena[x]
        nbase10alrevez[lon-x-1]= cadena[x]
    if nbase10 == nbase10alrevez:
        
        nbase2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        nbase2alrevez = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        longitud=0
        h=1
        #convertir el numero a binario
        nn = i
        for k in range(20):
            if nn % 2 == 0:
                nbase2[20-k] = 0
            else:
                nbase2[20-k] = 1
            nn = int(nn/2)
        #obtenemos su longitud
        for l in range(20):
            if nbase2[l*h]==1:
                longitud = 20 - l
                h = 0
        for d in range(longitud+1):
            nbase2alrevez[20-d] = nbase2[20-longitud+d]
            if nbase2 == nbase2alrevez:
                suma += i
print("Suma: "+str(suma))

# RESUELTO  Mié, 23 de junio de 2021, 11:45
