
from random import randint, choices

def formato(numero):
    # asegurarse de tener 4 caracteres siempre
    # le das un numero y te devuelve un string
    numero = str(numero)
    if len(numero) == 0:
        numero += '    '
    elif len(numero) == 1:
        numero = ' ' + numero + '  '
    elif len(numero) == 2:
        numero = ' ' + numero + ' '
    elif len(numero) == 3:
        numero = ' ' + numero 
    return numero

def imprimir_tablero(matriz):
    # transformar matriz en tablero
    
    print(f'+----+----+----+----+')
    print(f'|{formato(matriz[0][0])}|{formato(matriz[0][1])}|{formato(matriz[0][2])}|{formato(matriz[0][3])}|')
    print(f'+----+----+----+----+')
    print(f'|{formato(matriz[1][0])}|{formato(matriz[1][1])}|{formato(matriz[1][2])}|{formato(matriz[1][3])}|')
    print(f'+----+----+----+----+')
    print(f'|{formato(matriz[2][0])}|{formato(matriz[2][1])}|{formato(matriz[2][2])}|{formato(matriz[2][3])}|')
    print(f'+----+----+----+----+')
    print(f'|{formato(matriz[3][0])}|{formato(matriz[3][1])}|{formato(matriz[3][2])}|{formato(matriz[3][3])}|')
    print(f'+----+----+----+----+')


def añadir_numero(matriz):

    fila_random = randint(0,3)
    columna_random = randint(0,3)

    if matriz[fila_random][columna_random] == '':
        matriz[fila_random][columna_random] = choices([2, 4], weights=[90, 10])[0]
    else:
        añadir_numero(matriz)

    return matriz


def izquierda(matriz):
    # quitar espacios 
    # si es el mismo numero  combinarlos en la direccion correcta
    # reconstruir vacios

    # quitar vacio
    matriz_vacia = []


    for fila in matriz:
        fila_vacia = []
        for i in fila:
            if i != '':
                fila_vacia.append(i)

        matriz_vacia.append(fila_vacia)

    #print(matriz_vacia)


    # sumar

    for i in range(4):
        for j in range(4):
            try:
                if matriz_vacia[i][j] == matriz_vacia[i][j+1]:
                    matriz_vacia[i][j] += matriz_vacia[i][j]
                    del matriz_vacia[i][j+1] 

            except IndexError:
                pass



    #print(matriz_vacia)

            

    # reconstruir

    for i in range(4):
        if len(matriz_vacia[i]) == 0:
            for _ in range(4):
                matriz_vacia[i].append('')
                
        elif len(matriz_vacia[i]) == 1:
            for _ in range(3):
                matriz_vacia[i].append('')

        elif len(matriz_vacia[i]) == 2:
            for _ in range(2):
                matriz_vacia[i].append('')

        elif len(matriz_vacia[i]) == 3:
            for _ in range(1):
                matriz_vacia[i].append('')


    if matriz == matriz_vacia:
        return matriz
    else:
        añadir_numero(matriz_vacia)
        matriz = matriz_vacia


    return matriz

def derecha(matriz):
    for i in matriz:
        i.reverse()

    
    #print(imprimir_tablero(matriz))
    matriz = izquierda(matriz)
   # print(izquierda(matriz))

    for i in matriz:
        i.reverse()

    
    return matriz

def rotar90(matrix):
    # rotar matriz

    fila1 = []
    fila2 = []
    fila3 = []
    fila4 = []

    fila1.append(matrix[0][3])
    fila1.append(matrix[1][3])
    fila1.append(matrix[2][3])
    fila1.append(matrix[3][3])


    fila2.append(matrix[0][2])
    fila2.append(matrix[1][2])
    fila2.append(matrix[2][2])
    fila2.append(matrix[3][2])


    fila3.append(matrix[0][1])
    fila3.append(matrix[1][1])
    fila3.append(matrix[2][1])
    fila3.append(matrix[3][1])


    fila4.append(matrix[0][0])
    fila4.append(matrix[1][0])
    fila4.append(matrix[2][0])
    fila4.append(matrix[3][0])

    matrix = []
    matrix.append(fila1)
    matrix.append(fila2)
    matrix.append(fila3)
    matrix.append(fila4)

    return matrix

def arriba(matriz):
    matriz = rotar90(matriz)
    matriz = izquierda(matriz)
    matriz = rotar90(matriz)
    matriz = rotar90(matriz)
    matriz = rotar90(matriz)
    return matriz

def abajo(matriz):
    matriz = rotar90(matriz)
    matriz = rotar90(matriz)
    matriz = rotar90(matriz)
    matriz = izquierda(matriz)
    matriz = rotar90(matriz)
    return matriz



# crear matriz
matriz = []
for i in range(4):
    fila = []  # nueva lista cada vez
    for j in range(4):
        fila.append('')
    matriz.append(fila)


añadir_numero(matriz)
añadir_numero(matriz)
imprimir_tablero(matriz)
    

while True:

    desplazamiento = input('[wasd] o [x]: ')

    if desplazamiento == 'a':
        matriz = izquierda(matriz)
        imprimir_tablero(matriz)
    elif desplazamiento == 'd':
        matriz = derecha(matriz)
        imprimir_tablero(matriz)
    elif desplazamiento == 'w':
        matriz = arriba(matriz)
        imprimir_tablero(matriz)
    
    elif desplazamiento == 's':
        matriz = abajo(matriz)
        imprimir_tablero(matriz)

        
    elif desplazamiento == 'x':
        break

