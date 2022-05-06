import time
import subprocess

def tempo_exec(num):
    cont_s = 0
    cont_3t = 0
    cont_6t = 0

    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoA.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate()
        tempo_final = time.time()
        cont_s += tempo_final-tempo_inicial
    media_s = cont_s/num     
    print('\nMedia do tempo de execução do algoritmoA: %f segundos' %media_s)


    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate('3')
        tempo_final = time.time()
        cont_3t += tempo_final - tempo_inicial
    media_3t = cont_3t/num
    print('\nMedia do tempo de execução do algoritmoB com 3 threads: %f segundos' %media_3t)
    
    for i in range(num):
        tempo_inicial = time.time()
        p = subprocess.Popen(['python', 'AlgoritmoB.py'], 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

        saida,_ = p.communicate('6')
        tempo_final = time.time()
        cont_6t += tempo_final - tempo_inicial
    media_6t = cont_6t/num
    print('\nMedia do tempo de execução do algoritmoB com 6 threads: %f segundos' %media_6t)
    
    speedup1 = (media_s/media_3t)
    speedup2 = (media_s/media_6t)
    print('\nSpeedup 3 threads: ',speedup1)
    print('\nSpeedup 6 threads: ',speedup2)

if __name__ == '__main__':
    tempo_exec(50) 
