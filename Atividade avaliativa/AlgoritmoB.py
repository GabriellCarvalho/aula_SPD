import threading
import numpy as np

def criar_matriz(m, n):
    matriz = np.random.choice([0, 2, 4, 8, 16, 32], size=(m, n))
    return matriz

def verificar_jogada(matriz):
    cima = False
    baixo = False
    esquerda = False
    direita = False
    texto = ''
    for i in range(399):
        for j in range(399):
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
        #print('\n',texto)
        return 1
    if(baixo == True):
        texto += ' BAIXO'
    if(esquerda == True):
        texto += ' ESQUERDA'
    if(direita == True):
        texto += ' DIREITA'
    if(cima == True):
        texto += ' CIMA'

    #print('\n',texto)
    return 0


def worker(num):
    for i in range(num):
        matriz = criar_matriz(400,400)
        #print(matriz)
        cont_none = verificar_jogada(matriz)
        #print('Não foi possível fazer a jogada %d vezes' %cont_none)

def exec(a):

    if (a == 3):
        threads = []
        for i in range(3):
            t = threading.Thread(target=worker, args=(2,))
            threads.append(t)
            t.start()
        for i in threads:
            i.join()

    if (a == 6):
        threads = []
        for i in range(6):
            t = threading.Thread(target=worker, args=(1,))
            threads.append(t)
            t.start()
        for i in threads:
            i.join()

if __name__ == '__main__':
    a = int(input('entre com a: '))
    exec(a)