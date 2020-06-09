
#201602882 (882)

def coll(numero):                       #FUNCION PARA EL ALGORITMO
    lista = []                          #SE CREA UNA LISTA
    while numero != 1:                  #CICLO MIENTRAS NUMERO NO SEA 1
        if numero % 2 == 0:             #SI EL NUMERO ES PAR
            lista.append(int(numero))
            numero = numero / 2
        else:                           #SI EL NUMERO ES IMPAR
            lista.append(int(numero))
            numero = (numero * 3) + 1
        if numero == 1:                 #SI EL NUMERO ES 1
            lista.append(int(numero))
    return(lista)


def fileWrite(fileName = 'collatz.txt'):
    archivo = open(fileName,'w')                            #SE ABRE EL ARCHIVO
    archivo.write('Sobreescribiendo archivo...\n')          #SE ESCRIBE EN EL ARCHIVO
    print('Espere, sobreescribiendo el archivo...')         
    for x in range (2 , 883):                               #SE RECORRE DE 2 A 882 (883 - 1)
        print(coll(x))
        archivo.write(str(coll(x)))                         #SE LLAMA LA FUNCION COLL
        archivo.write('\n')
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('Append finalizado')
fileWrite()