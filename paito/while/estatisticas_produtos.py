'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''
import os 
os.system('cls')


print('-'*50)
print(' ' * 15, 'LOJA SUPER BARATÃO', ' ' * 15)
print('-'*50)


me = -1
cont = 1
total = mais_de_1000 = 0
produto_menor = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continuar = ' '
    total = total + preco
    if (cont == 1):
        me = preco
        produto_menor = produto
    else:
        if preco < me:
            me = preco
            
    cont = cont + 1
    if preco > 1000:
        mais_de_1000+=1
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        print('------------- FIM DO PROGRAMA -------------')
        print(f'O total de compra foi: R${total:.2f}')
        print(f'Temos {mais_de_1000} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {produto_menor} que custa R${preco:.2f} ')
        break
