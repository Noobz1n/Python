'''

Fazer a tabuada de um número, se o numero for negativo, parar o programa.


'''
import os
os.system('cls')



while True:
    num = int(input('Qual número você quer saber a tabuada?  '))
    print('=' * 30)
    if num < 0:
            break
    else:
        for c in range (0, 10):
            c+=1
            print(f'{num} x {c} = {num*c}')    
    print('=' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
