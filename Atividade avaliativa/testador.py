import time
import subprocess

def tempo_exec(num):
    
    tempo_inicial = time.time()
    for i in range(num):
        p = subprocess.Popen(['python', 'AlgoritmoA.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate()

    tempo_final = time.time()

    print('\nTempo de execução do algoritmoA de %d vezes: %f segundos' %(num, (tempo_final - tempo_inicial)))

    tempo_inicial = time.time()
    for i in range(num):
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate()
    tempo_final = time.time()

    print('\nTempo de execução do algoritmoB de %d vezes: %f segundos' %(num, (tempo_final - tempo_inicial)))
    
tempo_exec(50) 
