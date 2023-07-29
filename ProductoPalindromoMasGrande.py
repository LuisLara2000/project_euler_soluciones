"""Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.

Encuentra el palíndromo más grande formado por el producto de dos números de 3 dígitos."""
normal= [0,0,0,0,0,0]
reves = [0,0,0,0,0,0]
pali = 0
for i in range(999):
    for j in range(999):
        numero = j*i
        lon = len(str(numero))
        for x in range(lon):
            normal[x] = str(numero)[x]
            reves[lon-x-1] = str(numero)[x]
        
        if normal == reves:
            if numero > pali:
                pali = numero
print(pali)          
# RESUELTO 16/06/2021

