'''Fazer um programa que leia os coeficientes de uma equação do segundo grau, calcular e mostrar a raizes dessa equação, calculo é o de bhaskara
'a' tem q ser diferente de zero, se for igual, imprimir que não é uma equação do segundo grau
se delta < 0 , nao existe real, imprimir que nao existe real
se delta = 0 , existe uma raiz real, imprimir a raiz e a mensagem 'Raiz única.'
se delta > 0 , existem duas raizes, imprimir as duas raizes '''
from math import sqrt


a = int(input("Insira o coeficiente 'a': "))
b = int(input("Insira o coeficiente 'b': "))
c = int(input("Insira o coeficiente 'c': "))

delta = (b**2) - 4 * a * c
x = (-(b) + sqrt(delta)) / 2
x2 = (-(b) - sqrt(delta)) / 2

if (a == 0):
    print('Não é equação do segundo grau')
else:
    if delta < 0:
        print('Não existe real.')
    elif delta == 0:
        print(x, x2)
    else:
        print(x, x2)