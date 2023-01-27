'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
import os 
os.system('cls')


resultado = {}

resultado['nome'] = str(input('Insira seu nome: '))
resultado['media'] = float(input('Insira sua média: '))
if resultado['media'] >= 7:
    resultado['situação'] = f'{resultado["nome"]} está aprovado!'
else:
    resultado['situação'] = f'{resultado["nome"]} está reprovado!'
print('-='*30)
print(f'''Nome = {resultado['nome']}
Média = {resultado['media']}
{resultado['situação']}''')
