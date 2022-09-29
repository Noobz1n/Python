'''Faça um programa que leia números inteiros até que o usuário digite 0. No final exiba a quantidade de números digitados, assim como a soma destes números e a média aritmética.'''


num = -5
soma = 0
qtd = 0

while (num != 0):
    num = int(input('Digite um número: '))
    if (num != 0):
        soma = soma + num
        qtd = qtd + 1
print(f'Soma = {soma}')
print(f'Quantidade = {qtd}')
media = soma / qtd
print(f'Média = {media}')