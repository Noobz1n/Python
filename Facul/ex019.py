"""
Faça um programa que exiba em ordem decrescente todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

"""

i = 1000

while (i >= 1):
    i = i - 1
    if (i % 5 == 0):
        print(i)
    elif (i % 3 == 0):
        print(i)