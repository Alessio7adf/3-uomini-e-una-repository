n = int(input("Inserire numero inferiore a 10.000: "))
while n >= 10000:
	print("valore errato")
	n = int(input("Inserire numero inferiore a 10.000: "))

divisore = 2
vettore = [1]
while divisore <= n:
	if n % divisore == 0:
		vettore.append(divisore)
	divisore += 1

print("divisori del numero", n, ":", vettore)
