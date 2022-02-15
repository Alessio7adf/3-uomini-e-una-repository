import random

NUMELE, MIN, MAX = 15, 10, 99
vettore = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

SUP = 0
while True:
	try:
		SUP = int(input(f"inserire numero compreso tra {MIN} e {MAX}: "))
		if not MIN < SUP < MAX:
			print("valore errato\n")
		else:
			break
	except ValueError:
		print("valore errato\n")

print("vettore prima:", vettore)

for i in vettore:
	if i < SUP:
		vettore.pop(vettore.index(i))

vettore.sort(reverse=True)

print("vettore dopo:", vettore)
