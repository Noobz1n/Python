'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:                                                                                                                                         A) Quantos números foram digitados.      
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

import os
os.system('cls')

lista = []


while True:
    n = lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        print('-='*30)
        print(f'Os valores digitados foram: {lista}')
        print('-='*30)
        print(f'Você digitou {len(lista)} valores.')
        print('-='*30)
        print(f'Valores na ordem decrescente: {sorted(lista, reverse=True)}')
        print('-='*30)
        if 5 in lista:
            print(f'O valor 5 está na lista.')
            print('-='*30)
        else:
            print(f'O valor 5 não está a lista.')
            print('-='*30)
        break
    
    
