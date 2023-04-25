# Escreva um programa em Python que leia uma lista de números e um número x e imprima se o número x está na lista. 
listaNumeros = [4,5,2,1,8,46,43,28,10,50,0,1,9]
num = int(input('Digite um numero: '))
for x in listaNumeros:
    if x == num:
        print('ta na lista')
        break
else:
    print('nao esta na lita')
    