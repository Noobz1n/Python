'''
Faça um programa que calcule o fatorial de um número. EX: 6! = 6*5*4*3*2*1 = 720
'''
import os 
os.system('cls')



total = 1
cont = 1


fat = int(input('Digite o número que deseja o fatorial: '))
while (cont <= fat):
    total = total * cont
    cont = cont + 1
    print(total)