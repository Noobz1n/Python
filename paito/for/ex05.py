# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. 
s = 0
c = 0
for numeros in range (1, 7):
    nums = int(input(f'Digite o {numeros} valor: '))
    if (nums % 2 == 0):
        s+=nums
        print(f'A soma dos números pares digitado é igual a: {s}')
        print('')
    else:
        print('Numero ímpar, descartado.')
        print('')
        