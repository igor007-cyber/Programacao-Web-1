#Escreva um programa em Python que leia uma lista de números e imprima apenas os números pares da lista.
listaNumeros = [4,5,2,1,8,46,43,28,10,50,0,1,9]
listaPares = []
for lista in listaNumeros:
    if lista%2 == 0:
        listaPares.append(lista)
print(f'lista de pares são: {listaPares}')