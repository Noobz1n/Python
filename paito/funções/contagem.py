'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
import os
from time import sleep
os.system('cls')


def linhas():
    print('-='*15)
    



def contador(a, b, c):
    for conta in range(a, b+1, c):
        print(conta)
        sleep(0.5)
        


linhas()
print('Contagem de 1 até 10 de 1 em 1: ')
contador(1, 10, 1)
linhas()

print('Contagem de 10 até 0 de 2 em 2: ')
contador(10, -2, -2)
linhas()


print('Agora é a sua vez: ')
n1 = int(input('Insira o valor do começo da contagem: '))
n2 = int(input('Insira o valor do fim da contagem: '))
n3 = int(input('Insira o passo da contagem: '))

if n1 > 0 and n2 < 0:
    n2 = n2 + (-2)
if n3 == 0:
    n3 = -1

contador(n1, n2, n3)
linhas()