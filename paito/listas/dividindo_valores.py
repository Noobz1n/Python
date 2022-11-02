'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
import os
os.system('cls')




lista = []
lista_par = []
lista_impar= []

while True:
    n = lista.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
for i, valores in enumerate(lista):
    if valores % 2 == 0:
        lista_par.append(valores)
    else:
        lista_impar.append(valores)

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {lista_par}')
print(f'A lista de ímpares é: {lista_impar}')