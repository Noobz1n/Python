'''


Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.



'''
import os
import random

os.system('cls')



vencer = 0


print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
while True:
    num = int(input('Diga um valor: '))
    par_impar = ' '


    computador = random.randint(0, num)
    soma = num + computador
    while par_impar not in 'PI':
        par_impar = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    if (soma % 2 == 0) and par_impar == 'I':
        print('----------------------------------------------------------')

        print(f'Você jogou {num} e o computador {computador}. Total de {soma}. Deu par')

        vencer+=1
        print(f'''Você venceu {vencer}x
        
        
        ''')
    elif (soma % 2 > 0) and par_impar == 'P':
        print('----------------------------------------------------------')
        print(f'Você jogou {num} e o computador {computador}. Total de {soma}. Deu ímpar')
        vencer+=1
        print(f'''Você venceu {vencer}x
        
        
        ''')
    else:
        print(f'Você jogou {num} e o computador {computador}. Total de {soma}. Deu ímpar')
        print('''Você PERDEU!!!
        
        
        
        ''')
        print('GAME OVER!!!')
        print(f'Você venceu {vencer}x')
        break
