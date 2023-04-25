# Escreva um programa em Python que leia uma lista de números e imprima a soma dos números.
listaNumeros = [4,5,2,1,8,46,43,28,10,50,0,1,9]
somaNumeros = 0
for x in listaNumeros:
    somaNumeros += x
print(f'Soma dos numeros: {somaNumeros}')