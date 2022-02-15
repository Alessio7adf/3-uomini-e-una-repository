vettore = []

numeri = 10
for i in range(numeri):
	while True:
		try:
			vettore.append(int(input(f"inserire {i + 1}° numero: ")))
			break
		except ValueError:
			print("valore errato\n")

vettore = list(dict.fromkeys(vettore))
print(vettore)
