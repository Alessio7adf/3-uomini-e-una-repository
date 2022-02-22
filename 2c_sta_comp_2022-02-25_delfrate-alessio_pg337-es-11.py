import random

NUMELE, MIN, MAX = 15, 2, 8
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

presenze_numeri = {}
for i in vettore:
	if not presenze_numeri.keys().__contains__(i):
		presenze_numeri[i] = 1
	else:
		presenze_numeri[i] += 1

vettore.clear()

for i in sorted(presenze_numeri, key=presenze_numeri.get, reverse=True):
	for j in range(presenze_numeri[i]):
		vettore.append(i)

print("vettore:", vettore)
