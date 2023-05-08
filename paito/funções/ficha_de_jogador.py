'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
import os
os.system('cls')


def ficha(jogador="<desconhecido>", gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


nome = input('Nome do Jogador: ')
num_gols = input('Número de Gols: ')
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0

if nome.strip() == '':
    ficha(gols=num_gols)
else:
    ficha(nome, num_gols)
    