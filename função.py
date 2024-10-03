#Criar uma função que receba uma lista de números e retorne a soma dos números ímpares da lista.

import random 

lista = list(range(1, 21))

for i in range(len(lista)):
    lista[i] += random.randint(1, 20)

print(lista)

def somar(lista):
    soma = 0
    for numero in lista:
        if (numero % 2 != 0):
            soma += numero
        elif (numero % 2 == 0):
            print('numero par')
    return soma 

soma = somar(lista)

print(soma)


