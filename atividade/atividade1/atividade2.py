# Escreva um programa em Python que imprima os números ímpares de 1 a 20.
x = []
for y in range(1,21,1):
    if y%2 == 1:
        x.append(y)

for y in x:
    print(y)