
#201602882 (882)

def coll(numero):                       #FUNCION PARA EL ALGORITMO
    lista = []                          #SE CREA UNA LISTA
    while numero != 1:                  #CICLO MIENTRAS NUMERO NO SEA 1
        if numero % 2 == 0:             #SI EL NUMERO ES PAR
            lista.append(numero)
            numero = numero / 2
        else:                           #SI EL NUMERO ES IMPAR
            lista.append(numero)
            numero = (numero * 3) + 1
        if numero == 1:                 #SI EL NUMERO ES 1
            lista.append(numero)
    return(lista)

for x in range (2 , 883):               #RECORRER LOS NUMEROS DESDE EL 2 HASTA 883-1(882)
    print(coll(x))