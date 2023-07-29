import math 

def combinaciones(n,r):
    resultado = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    return resultado

def principal():
    azules = 0
    verde = 0
    rojos = 0
    baldozas = 50
    azulejos = 1
    for i in range(25):
        baldozas -= 1        
        print(str(baldozas)+"C"+str(azulejos))
        rojos += combinaciones(baldozas, azulejos)
        azulejos += 1
    print("--")
    baldozas = 50
    azulejos = 1
    for k in range(16):
        baldozas -= 2
        print(str(baldozas)+"C"+str(azulejos))
        verde += combinaciones(baldozas, azulejos)
        azulejos += 1
    baldozas = 50
    azulejos = 1
    print("--")
    for p in range(12):
        baldozas -= 3
        print(str(baldozas)+"C"+str(azulejos))
        azules += combinaciones(baldozas, azulejos)
        azulejos += 1

    print(rojos)
    print(verde)
    print(azules)
    #sumarle 2 al final
    print("resultado: "+str(rojos+verde+azules))

principal()

