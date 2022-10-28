'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''
import os
os.system('cls')



times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Coritiba','Avaí','Ponte preta','Atlético-GO')

print('-=' * 60)
print(f'Listas de time do Brasileirão: {times}')
print('-=' * 60)
print(f'Os 5 primeiros times são: {times[0:6]}')
print('-=' * 60)
print(f'Os 4 últimos são: {times[16:]}')
print('-=' * 60)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 60)
print(f'Chapecoense está na {len(times[8])} posição')
