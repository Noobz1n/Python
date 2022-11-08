import os
os.system('cls')


def linhasTestes(txt):
    print('-=' * 50)
    print(txt)
    print('-=' * 50)    


linhasTestes('TESTE')

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

def soma(a, b):
    s = a + b
    print(s)

soma(2,5)
soma(x, y)



def teste(* num):
    print('----------------')
    tam = len(num)
    print(f'Recebi os valores: {num} e são ao todo {tam} números')
teste(5, 2 , 5, 5)
teste(1, 5, 8)



valores = [5, 7, 14, 10, 11]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos+=1
    print(lst)
dobra(valores)



def somaValores(* numss):
    s = 0
    for numeros in numss:
        s = s + numeros
        
    print(s)

somaValores(5, 5, 5)
somaValores(9, 5)