'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
import os 
os.system('cls')




palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for pos in palavras:
    print(f'\nNa palavra {pos} temos ', end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end='')
