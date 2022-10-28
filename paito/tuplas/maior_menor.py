'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

Aula Anterior
'''

from random import randint
import os

os.system('cls')


numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados são: {numeros}') # Aqui os números vão aparecer com os parenteses da tupla

for n in numeros:     # Aqui os números vão aparecer sem os parenteses, por causa do laço de repetição
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')