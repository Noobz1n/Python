'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.


Um número inteiro é par se ele é divisível por 2, ou seja, se a divisão desse número por 2 tem resto igual a 0.
'''
import os
os.system('cls')




# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))
# num3 = int(input('Digite mais um número: '))
# num4 = int(input('Digite o último número: '))
# valores = (num1, num2, num3, num4)

# Forma mais fácil de fazer o input, economizar linha, memoria e deixar o programa mais rapido:
valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))



print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)} posição')
else: 
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for i in valores:
    if i % 2 == 0:
        print(f'{i}', end=' ')