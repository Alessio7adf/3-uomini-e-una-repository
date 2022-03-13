import random

NUMELE, MIN, MAX = 15, 2, 20
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

print("vettore prima del ribaltamento:\t", vettore)
vettore.reverse()
print("vettore dopo il ribaltamento:\t", vettore)
