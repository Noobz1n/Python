'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
import os

# Não consegui importar a biblioteca datetinme

os.system('cls')


cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['ano'] = int(input('Ano de nascimento: '))
idade = 2023 - cadastro['ano']
cadastro['carteira'] = int(input('Carteira de trabalho (0 se não tem): '))

if cadastro['carteira'] == 0 or idade < 18:
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
else:
    cadastro['ano_contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = int(input('Salário: R$'))
    aposentar = idade + ((cadastro['ano_contratacao'] + 35) - 2023) # Não consegui importar a biblioteca datetinme
    print('-=' * 50)
for key, valor in cadastro.items():
    print(f' - {key} tem o valor {valor}')