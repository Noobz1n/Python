'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
'''



import os
os.system('cls')


larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
def area(a, b):
    area = a * b
    print(f'A área de um terreno {a}x{b} é de {area}m².')

area(larg, comp)