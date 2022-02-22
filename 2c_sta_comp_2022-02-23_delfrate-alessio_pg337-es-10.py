import random

NUMELE, MIN, MAX = 15, 1, 100
vettore = []

for i in range(NUMELE):
  vettore.append(random.randint(MIN, MAX))

n = input("Inserire valore: ")
volte = 0

for i in vettore:
  if i == n:
    volte +=1

print("numero di volte in cui il valore appare nel vettore", vettore, ":", volte)
