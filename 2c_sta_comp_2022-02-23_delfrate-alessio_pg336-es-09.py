import random

NUMELE, MIN, MAX = 15, 1, 20
vettore = []

for i in range(NUMELE):
    n = random.randint(MIN, MAX)
    while not n in vettore:
        n = random.randint(MIN, MAX)
    vettore.append(n)

print("vettore:", vettore)
