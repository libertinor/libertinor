import random
import time

def shell_sort(v):

    h = len(v) // 2 #distancia
    while h > 0:
        i = h
        while i < len(v):
            tempo = v[i]
            trocou = False
            j = i - h
            while j >= 0 and v[j] > tempo:
                v[j+h] = v[j]
                trocou = True
                j -= h

            if trocou:
                v[j+h] = tempo

            i += 1

        h = h // 2

vetor = list(range(0, 10000))
random.shuffle(vetor)
antes = time.time()
shell_sort(vetor)
depois = time.time()
total = (depois - antes)*1000

print(vetor)

print("o tempo total foi: %0.2f ms" % total)