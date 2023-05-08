'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-las dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
'''
from random import randint
import os
os.system('cls')


sorteados = []
cont = 1

# Função pra sortear 5 númeroos em uma lista
while cont <= 5:
    sorteados.append(randint(0, 10))
    cont+=1

def sorteia():
    print(f'Valores sorteados da lista: {sorteados}')
sorteia()


# Função pra somar os numeros pares da lista
def somaPar():
    soma = 0
    print(f'Numeros pares da lista:', end=' ')
    for pares in sorteados:
        if pares % 2 == 0:
            print(f'{pares} ', end='')
            soma = soma + pares
    print(f'\nA soma de todos os números pares da lista é: {soma}')

somaPar()