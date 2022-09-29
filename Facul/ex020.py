''' 
Elabore um programa que faça a leitura de vários números inteiros até que se digite um número negativo. O programa tem de
retornar o maior e o menor número lido
'''

ma = -1
me = -1
cont = 1
num = 404

while (num >= 0):
    num = int(input('Digite um número inteiro: '))
    if (cont == 1):
        ma = num
        me = num
    else:
        if (num > ma):
            ma = num
        if ((num < me) and (num >= 0)):
            me = num
    cont = cont + 1
if (cont <= 0) and (cont == 2):
    print('Nenhum número digitado!')
print(f'Maior = {ma}')
print(f'Menor = {me}')