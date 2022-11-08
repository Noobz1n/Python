'''
Faça um programa que tenha uma função chamada (escreva), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel
'''
import os
os.system('cls')








while True:
    adaptar = input('Insira o texto que deseja adaptar: ')

    def escreva(txt):
        tam = len(adaptar)
        print('~'*(tam+2))
        print(txt.center(tam+2))
        print('~'*(tam+2))
    escreva(adaptar)