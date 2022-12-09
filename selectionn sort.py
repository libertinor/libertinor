import random
import time
def selection_sort(v) :
    i = 0
    while i < len(v) - 1:
        menor = i
        j = i + 1
        #em busca do menor elemento
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j +=1

        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        i += 1

vetor = list(range(0, 10000))
random.shuffle(vetor)
antes = time.time()
selection_sort(vetor)
depois = time.time()
total = (depois - antes)*1000

#print(vetor)
print ("o tempo total para ordenar: %0.2f ms " % total)
