import random

NUMELE, MIN, MAX = 15, 2, 20
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

vettore = [5, 2, 17, 12, 8, 15, 2, 14, 12, 11, 8, 9, 4, 3, 13]

pivot = vettore[random.randint(0, NUMELE - 1)]

pivot = vettore[9]

print("pivot:", pivot)
print("vettore prima:\t", vettore)

for i in range(NUMELE):

	if vettore[i] > pivot and i < vettore.index(pivot):
		vettore.insert(vettore.index(pivot) - 1, vettore.pop(i))
	elif vettore[i] < pivot and i > vettore.index(pivot):
		vettore.insert(vettore.index(pivot) + 1, vettore.pop(i))

print("vettore dopo:\t", vettore)
