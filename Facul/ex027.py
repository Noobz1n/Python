'''
4) Escreva um programa que o usuário digite um valor entre 1 e 999, passe esse valor para a função
que calculará e retornará o número ao contrário e então mostre-o na tela.
Ex: Número lido = 123
Número calculado = 321
'''

def inverter():
    num = int(input('Digite o número que deseja inverter: '))
    num = str(num)
    print(num[::-1])
inverter()