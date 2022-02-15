import random

NUMELE, MIN, MAX = 15, 1, 100
vettore, posizioni_errate = [], []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

for i in range(NUMELE):
	if i & 1:
		if not vettore[i] & 1:
			posizioni_errate.append(f"numero {vettore[i]} alla posizione {i}")
	else:
		if vettore[i] & 1:
			posizioni_errate.append(f"numero {vettore[i]} alla posizione {i}")

print("vettore:", vettore)
for i in posizioni_errate:
	print(i)
