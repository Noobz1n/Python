'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''


import os
os.system('cls')


lista = []

for valor in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

print(lista)

for c, v in enumerate(lista):
    print(f'No índice {c}, tem o valor: {v}.')

print(f'O maior valor da lista é: {max(lista)}')
print(f'O menor valor da lista é: {min(lista)}')