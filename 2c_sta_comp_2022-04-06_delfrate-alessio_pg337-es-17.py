import random

NUMELE = 10000
vettore = [i for i in range(NUMELE)]
random.shuffle(vettore)
vettoreSort = [0] * NUMELE

print("vettore prima del sort\t", vettore)

for i in range(NUMELE):
	conta = 0
	n = vettore.pop(i)
	vettore.insert(0, n)
	for j in vettore[1:]:
		if j < n:
			conta += 1
	vettoreSort[conta] = n

print("vettore dopo il sort\t", vettoreSort)
