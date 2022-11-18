'''
1) Terminar a calculadora, adicionando mais 2 funções:
a) Potenciação (usuário digita 2 valores)
b) Fatorial (usuário digita apenas 1 valor)
'''


'''
1) Terminar a calculadora, adicionando mais 2 funções:
a) Potenciação (usuário digita 2 valores)
b) Fatorial (usuário digita apenas 1 valor)
'''



def calculadora():
    opc = int(input('''Selecione a opção:
[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[5] - Potenciação 
[6] - Fatorial
'''))
    if opc == 6:
        total = 1
        cont = 1
        fat = int(input('Digite o número que deseja o fatorial: '))
        while (cont <= fat):
            total = total * cont
            cont = cont + 1 
        print(f'Fatorial de {fat} = {total}')
    
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
  
    if opc == 1:
        total = n1 + n2
        print(f'{n1} + {n2} = {total}')
    elif opc == 2:
        total = n1 - n2
        print(f'{n1} - {n2} = {total}')
    elif opc == 3:
        total = n1 * n2
        print(f'{n1}x{n2} = {total}')
    elif opc == 4:
        total = n1 / n2
        print(f'{n1}/{n2} = {total}')
    elif opc == 5:
        total = n1**n2
        print(f'{n1}**{n2} = {total}')
calculadora()