import random
import time

def insertion_sort(v):
    i = 1
    while i < len(v):
        tempo = v[i]
        trocou = False
        j = i - 1
        while j >= 0 and v[j] > tempo:
            v[j+1] = v[j]
            trocou = True
            j -= 1

        if trocou:
            v[j+1] = tempo

        i += 1

vetor = list(range(0, 10000))
random.shuffle(vetor)
antes = time.time()
insertion_sort(vetor)
depois = time.time()
total = (depois - antes)*1000

print(vetor)

print("o tempo total foi: %02f ms" %total)




