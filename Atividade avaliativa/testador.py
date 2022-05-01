import sys
import time
import os

def tempo_exec(var):
    
    tempo_inicial = time.time()
    for i in range(var):
        os.system('python AlgoritmoA.py')

    tempo_final = time.time()

    print('\nTempo de execução do algoritmoA de %d vezes: %f segundos' %(var, (tempo_final - tempo_inicial)))

    tempo_inicial = time.time()
    for i in range(var):
        os.system('python AlgoritmoB.py')

    tempo_final = time.time()

    print('\nTempo de execução do algoritmoB de %d vezes: %f segundos' %(var, (tempo_final - tempo_inicial)))
    
tempo_exec(50)