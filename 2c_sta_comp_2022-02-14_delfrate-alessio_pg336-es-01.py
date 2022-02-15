import random

NUMELE, MIN, MAX = 15, 10, 80
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

print("vettore prima dello scambio:\t", vettore)

posizione_massimo, posizione_minimo = vettore.index(max(vettore)), vettore.index(min(vettore))
vettore[posizione_massimo], vettore[posizione_minimo] = vettore[posizione_minimo], vettore[posizione_massimo]

print("vettore dopo lo scambio:\t\t", vettore)
print(f"numeri scambiati: {vettore[posizione_massimo]}, {vettore[posizione_minimo]}")
