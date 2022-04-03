import random

NUMELE, MIN, MAX = 15, 2, 20
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

pivot = random.randint(0, NUMELE - 1)

print("indice pivot:\t", pivot)
print("valore pivot:\t", vettore[pivot])
print("vettore prima:\t", vettore)

pivot = vettore.pop(pivot)

vettore.insert(0, pivot)

for i in range(1, NUMELE):

	if vettore[i] <= pivot:
		vettore.insert(0, vettore.pop(i))
		i -= 1

print("vettore dopo:\t", vettore)
