'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

import os 
os.system('cls')


homens = mulheres = pessoas_18 = 0
print('''-------------------------
CADASTRE UMA PESSOA
-------------------------''')

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = input('Sexo:  [M/F] ').strip().upper()[0]
        if idade >= 18:
            pessoas_18+=1
            
        if sexo == 'M':
            homens+=1

        if idade < 20 and sexo == 'F':
            mulheres+=1


    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {pessoas_18}\nAo todo temos {homens} homens cadastrados\nE temos {mulheres} mulheres com menos de 20 anos')
