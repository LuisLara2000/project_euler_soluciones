# 42 NUMEROS TRIANGULARES CODIFICADOS
import math

# leemos el archivo
archivo = open('palabras.txt', 'r')
palabras = archivo.read()
archivo.close()

i=suma=triangular=numero=0
palabraActual=""

while palabras[i] != "$":
    if ord(palabras[i]) != 44: # valor en acsii de la coma
        if ord(palabras[i]) != 34:
            palabraActual += palabras[i]
    else:# una vez capturada la palabra
        for k in range(len(palabraActual)):
            suma += int(ord(palabraActual[k])-64)
        numero = suma*2
        # aplico el numero a la formula
        resultado = math.sqrt((1+4*numero))
        resultadoStr = str(resultado)
        pos = str(resultado).find(".")

        if resultadoStr[pos+1] == "0":
            if int(len(resultadoStr)-pos)==2:
                triangular += 1

        suma = 0
        numero = 0
        palabraActual = ""
    i+=1

print(str(triangular)) 

