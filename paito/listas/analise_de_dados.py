'''
Faça um programa que leia nome e peso de várias pessoas,  guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.                             
B) Uma listagem com as pessoas mais pesadas.                                                                                                    C) Uma listagem com as pessoas mais leves.
'''
import os
os.system('cls')


tot_pessoas = 0
maior = menor = 0
cadastro = []
infos = []
while True:
    cadastro.append(input('Nome: '))
    cadastro.append(float(input('Peso: ')))
    if len(infos) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    infos.append(cadastro[:])
    cadastro.clear()
    resp = input('Quer continuar? [S/N] ')
    tot_pessoas+=1
    if resp in 'Nn':
        break

print(f'Ao todo temos {tot_pessoas} cadastradas')
print(f'O maior peso foi de {maior}kg, pessoas:', end=' ')
for p in infos:
    if p[1] == maior:
        print(f'{p[0]}')

print(f'O menor peso foi de {menor}kg, pessoas:', end=' ')
for p in infos:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

# print(f'O maior peso foi de: {max(infos)}')   forma de pegar o maior peso junto com o nome, o min não funciona se botar os dois maiores pesos iguais
