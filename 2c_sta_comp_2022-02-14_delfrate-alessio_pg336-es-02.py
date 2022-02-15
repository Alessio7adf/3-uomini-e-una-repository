import random

numeri_da_generare, MIN, MAX = 30, 0, 50
pari, dispari = [], []

for i in range(numeri_da_generare):
	numero = random.randint(MIN, MAX)
	if numero & 1:
		dispari.append(numero)
	else:
		pari.append(numero)

print("numeri pari:\t", pari)
print("numeri dispari:\t", dispari)
