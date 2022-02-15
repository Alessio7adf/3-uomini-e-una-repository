def insersci_intero(prompt: str):
	r = 0
	while True:
		try:
			r = int(input(prompt))
			break
		except ValueError:
			print("valore errato\n")
	return r


N = insersci_intero("numeri da inserire: ")
vetA = []
for i in range(N):
	vetA.append(insersci_intero(f"{i + 1}° numero: "))

for i in vetA:
	print(i, ":", "*" * i)
