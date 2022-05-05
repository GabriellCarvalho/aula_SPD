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
    tempo_S = tempo_final-tempo_inicial       
    print('\nMedia do tempo de execução do algoritmoA: %f segundos' ,(tempo_final-tempo_inicial))

    tempo_inicial = time.time()
    for i in range(num):
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate('3')
    tempo_final = time.time()

    print('\nTempo de execução do algoritmoB com 3 threads: %f segundos',(tempo_final-tempo_inicial))
    

    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate('6')
        tempo_final = time.time()
    print('\nTempo de execução do algoritmoB com 6 threads: %f segundos' ,(tempo_final-tempo_inicial))
    tempo_P = tempo_final-tempo_inicial
    speedup = tempo_S/tempo_P
    print('\nSpeedup: ',speedup)
    
tempo_exec(50) 
