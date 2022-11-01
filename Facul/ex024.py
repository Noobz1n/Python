'''
Fazer um programa que leia um número IP e retorne se ele está ativo ou não.
'''

import subprocess

ip = input('Digite um número IP: ')
resposta = str(subprocess.check_output(["ping", "-n", "1", ip]))
if resposta.find == -1:
    print(f'{ip} : FORA')
else:
    print(f'{ip} : PINGOU') 