'''
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele
próprio. Exemplo: os divisores de 66 são: 1+2+3+6+11+22+33 = 78.



Falta saber como remover o ultimo do divisor
'''
import os
os.system('cls')



num = int(input('Digite um número: '))
i = num - 1
soma = 0
while (i >= 1):
    if (num % i == 0):
        soma = soma + i
        print(i)
    i = i - 1
print(soma)