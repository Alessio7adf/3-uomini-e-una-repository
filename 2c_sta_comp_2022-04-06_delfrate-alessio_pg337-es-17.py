import random

NUMELE, MIN, MAX = 15, 2, 20
vettore = []
vettoreSort = []

for i in range(NUMELE):
	n = random.randint(MIN, MAX)
	while vettore.__contains__(n):
		n = random.randint(MIN, MAX)
	vettore.append(n)
	vettoreSort.append(0)

massimo = max(vettore)

for i in range(NUMELE):
	conta = 0

	for j in range(NUMELE):
		if i != j:
			if vettore[j] < vettore[i]:
				conta += 1

	vettoreSort[conta] = vettore[i]
print("vettore prima del sort\t", vettore)
print("vettore dopo il sort\t", vettoreSort)
