# Escreva um programa em Python que leia uma lista de números e imprima apenas os números ímpares da lista.
listaNumeros = [4,5,2,1,8,46,43,28,10,50,0,1,9]
listaImpares = []
for lista in listaNumeros:
    if lista%2 == 1:
        listaImpares.append(lista)
print(f'lista de pares são: {listaImpares}')