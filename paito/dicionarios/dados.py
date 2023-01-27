'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
import os
from random import randint
from time import sleep
from operator import itemgetter

os.system('cls')

valores = dict()
ranking = dict()

valores = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
}
for k, v in valores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.7)
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)

sleep(0.7)

print('-=' * 50)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
