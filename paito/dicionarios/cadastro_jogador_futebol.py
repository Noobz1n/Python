'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
import os
os.system('cls')


lista = dict()
gols = list()
i = 1
tot_gols = 0


lista['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {lista["jogador"]} jogou? '))
while i <= partidas:
    lista['gols'] = int(input((f'Quantos gols na partida {i}? ')))
    gols.append(lista['gols'])
    lista['gols'] = gols
    lista['total'] = sum(lista['gols'])
    i+=1
print('-=' * 50)
print(lista)
print('-=' * 50)
for k, v in lista.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 50)
print(f'O jogador {lista["jogador"]} jogou {partidas+1} partidas.')
for i, v in enumerate(lista['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {sum(lista["gols"])} gols.')
