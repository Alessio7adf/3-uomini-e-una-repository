import random

NUMELE, MIN, MAX = 15, 10, 20
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))


def sposta(x: int, destra: bool):
	v = []

	if destra:
		for i in range(NUMELE):
			v.append(vettore[i - x])
	else:
		for i in range(NUMELE - x):
			v.append(vettore[i + x])
		for i in range(x):
			v.append(vettore[i])

	return v


print("vettore prima spostamento:\t", vettore)
print("vettore dopo spostamento:\t", sposta(3, True))
