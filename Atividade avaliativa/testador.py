import time
import subprocess

def tempo_exec(num):
    cont = 0
    media = 0
    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoA.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate()

        tempo_final = time.time()
        cont = cont +  (tempo_final-tempo_inicial)
    media = cont/num 
    print('\nMedia do tempo de execução do algoritmoA: %f segundos' %media)

    cont = 0
    media = 0
    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate('3')
        tempo_final = time.time()
        cont = cont +  (tempo_final-tempo_inicial) 
    media = cont/num
    print('\nMedia do tempo de execução do algoritmoB com 3 threads: %f segundos' %media)
    
    cont = 0
    media = 0
    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate('6')
        tempo_final = time.time()
        cont = cont +  (tempo_final-tempo_inicial) 
    media = cont/num
    print('\nMedia do tempo de execução do algoritmoB com 6 threads: %f segundos' %media)
    
tempo_exec(50) 
