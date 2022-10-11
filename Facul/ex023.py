'''

Faça um programa que verifique se um número digitado é primo ou não

'''


i = 0


while (i == 0):
    num = int(input('Digite um número: '))
    if ((num % 2 != 0 or num == 2)):
        print(f'{num} é primo!')
    else:
        print(f'{num} não é primo!')