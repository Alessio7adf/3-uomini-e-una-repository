import random

n = random.randint(0, 255)
s = str(bin(n))
vettore = []
for i in range(2, len(s)):
	vettore.append(int(s[i]))

for i in range(8 - len(vettore)):
	vettore.insert(0, 0)

print(vettore)
