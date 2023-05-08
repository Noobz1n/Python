'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import datetime
import os
os.system('cls')



def voto(ano):
    hoje = datetime.now()
    idade = hoje.year - ano
    if(idade < 18):
        print(f'Com {idade} anos: VOTO NEGADO.')
    if (idade >= 18 or idade < 70):
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    if(idade >= 70):
        print(f'Com {idade} anos: VOTO OPCIONAL.')\

ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)