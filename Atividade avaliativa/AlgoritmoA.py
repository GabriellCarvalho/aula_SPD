import numpy as np

def verifica(matriz):
    cima = False
    baixo = False
    esquerda = False
    direita = False
    texto = ''
    for i in range(4):
        for j in range(4):
            if(i != 0):
                if(matriz[i][j] == matriz[i-1][j] or matriz[i-1][j] == 0):
                    cima = True
            if(j != 0):
                if(matriz[i][j] == matriz[i][j-1] or matriz[i][j-1] == 0):
                    esquerda = True 
            if(i != 3):
                if(matriz[i][j] == matriz[i+1][j] or matriz[i+1][j] == 0):
                    baixo = True
            if(j != 3):
                if(matriz[i][j] == matriz[i][j+1] or matriz[i][j+1] == 0):
                    direita = True                    
    if(cima == False and esquerda == False and baixo == False and direita == False):
        texto = 'NONE'
    if(baixo == True):
        texto += ' BAIXO'
    if(esquerda == True):
        texto += ' ESQUERDA'
    if(direita == True):
        texto += ' DIREITA'
    if(cima == True):
        texto += ' CIMA'
    
    print(texto)

def criar_matriz(m,n):
    matriz = np.random.choice([0,2,4,8,16,32], size=(m,n))
    return matriz


matriz1 = criar_matriz(4,4)
matriz2 = criar_matriz(4,4)
matriz3 = criar_matriz(4,4)
matriz4 = criar_matriz(4,4)

print(matriz1)
verifica(matriz1)

print(matriz2)
verifica(matriz2)

print(matriz3)
verifica(matriz3)

print(matriz4)
verifica(matriz4)