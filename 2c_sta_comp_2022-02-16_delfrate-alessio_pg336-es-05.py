import math

n1, n2 = 0, 0
while True:
	try:
		n1 = int(input(f"inserire numero intero positivo: "))
		n2 = int(input(f"inserire numero intero positivo: "))
		if not (n1 > -1 and n2 > -1):
			print("valori errati\n")
		else:
			break
	except ValueError:
		print("valore errato\n")

print(f"quadrati perfetti tra {n1} e {n2}: ", end="")

if n1 > n2:
	n1, n2 = n2, n1

while not math.sqrt(n1).is_integer():
	n1 += 1

while not math.sqrt(n2).is_integer():
	n2 -= 1

q_perfetti = []
for i in range(n1, n2 + 1):
	if math.sqrt(i).is_integer():
		q_perfetti.append(i)

print(q_perfetti)
