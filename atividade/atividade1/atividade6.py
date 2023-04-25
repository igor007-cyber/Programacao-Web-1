#Escreva um programa em Python que leia um número inteiro e imprima a tabuada desse número (de 1 a 10).
num = int(input('Digite um numero pra fazer a tabuada: '))

for x in range(1,11):
    print(f'{num} x {x} = {num * x}')