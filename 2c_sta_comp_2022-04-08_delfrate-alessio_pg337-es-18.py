import random

NUMELE, MIN, MAX = 15, 2, 20
vettore = []
vettore2 = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

massimo = max(vettore)

for i in range(massimo + 1):
	if vettore.__contains__(i):
		vettore2.append(i)
print(vettore)
print(vettore2)
