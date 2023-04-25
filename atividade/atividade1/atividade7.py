#Escreva um programa em Python que leia um número inteiro e imprima a sequência de Fibonacci até esse número.
num = int(input('Digite um numero:'))
# aNum = 0
# dNum = 1
# find = 0
# resultado = 0
# while num > find:
#     find = aNum + dNum
#     aNum = dNum
#     dNum = find   


def fib(num):
    if num < 2:
        return 1
    return fib(num-1) + fib(num-2)

print(fib(num))