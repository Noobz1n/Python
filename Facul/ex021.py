'''
Faça um programa que calcule e escreva o valor de S: 𝑆 = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99 / 50
'''


n1 = 1
n2 = 1
result = 0

while (n1 <= 97) and (n2 <= 49):
    n1 = n1 + 2
    n2 = n2 + 1
    print(f'S = {n1} / {n2} = {n1/n2:.5f}')