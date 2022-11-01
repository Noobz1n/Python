'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
import os
os.system('cls')


lista = []


while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor já existente na lista, não irá ser adicionado.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? ').strip().upper()[0]
    if continuar == 'N':
        print(f'Numeros na lista: {sorted(lista)}')
        break

