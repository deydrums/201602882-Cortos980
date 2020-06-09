
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
    archivo = open(fileName,'w') 
    archivo.write('Sobreescribiendo archivo...\n')
    print('Espere, sobreescribiendo el archivo...')
    for x in range (2 , 883):              
        print(coll(x))
        archivo.write(str(coll(x)))
        archivo.write('\n')
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('Append finalizado')

fileWrite()