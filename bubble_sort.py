import random
import time

def bubble_sort(v) :

    fim = len(v)

    while fim > 0:

        i = 0
        #percorrendo o vetor de 0 ate fim
        while i < fim-1:
            if v[i] > v[i+1]:
                #realizando a troca de posição atual pela proxima
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
                #print(v)
            i += 1

        fim -= 1

vetor = list(range(0, 10000))
random.shuffle(vetor)

#print(vetor)

antes = time.time()
bubble_sort(vetor)
depois = time.time()

total = (depois - antes)*1000

print ("A ordenação demorou %0.2f ms" % total)








