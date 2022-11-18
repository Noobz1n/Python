'''
Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros, seu programa tem que analisar todos os valores e dizer qual é o maior
'''

from time import sleep
import os
os.system('cls')


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(1, 5, 7, 8, 14)
maior(14, 15, 20)
maior(15, 16)
maior()