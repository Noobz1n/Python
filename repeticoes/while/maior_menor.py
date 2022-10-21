'''


Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


'''
import os
os.system('cls')


#Forma do guanabara

# resp = 'S'
# soma = quant = media = 0

# while resp in 'Ss':
#     num = int(input('Digite um número: '))
#     soma += num
#     quant += 1
#     if quant == 1:
#           maior = menor = num
#     else:
#         if num > maior:
#               maior = num
#         else:
#               menor = num
#     resp = input('Quer continuar? [S/N] ').upper().strip()[0]
# media = soma / quant
# print(f'Você digitou {quant} números e a média foi {media}')




ma = me = -1
cont = 1
num = 404
resposta = "S"
soma = 0
i = 0

while resposta == "S":
    num = int(input('Digite um número: '))
    i+=1 # Aqui da a quantidade de números digitados
    soma = soma + num
    resposta = input('Quer continuar? [S/N] ').upper()
    if (cont == 1):
        ma = num
        me = num
    else:
        if (num > ma):
            ma = num
        if ((num < me)):
            me = num
    cont = cont + 1
print(f'Você digitou {i} números e a média foi {soma/i:.2f}\nMaior número digitado: {ma}\nMenor Numero digitado: {me}')
