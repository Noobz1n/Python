'''
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele
próprio. Exemplo: os divisores de 66 são: 1+2+3+6+11+22+33 = 78.



Falta saber como remover o ultimo do divisor
'''
import os
os.system('cls')



i = 0
num = int(input('Digite um número: '))
while (i < num):
    i+=1
    if (num % i == 0):
        soma = i + i
        print(f'Divisores: {i}')
        print(f'Soma: {i} + {i} = {soma} \n')