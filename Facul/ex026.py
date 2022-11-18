'''
Escreva um programa que o usuário adicione itens em uma lista depois chame uma função que
passando esta lista, retorne o maior valor contido nela e mostre na tela
'''

def lista():
    itens = []
    while True:        
        parar = ' '
        cont = 0

        add_item = input('Digite o nome do item: ')
        itens.append(add_item)

        valor_item = float(input(f'Digite o valor do {add_item}: '))
        itens.append(valor_item)

        if cont == 0:
            maior = valor_item
        else:
            if valor_item > maior:
                maior = valor_item
        cont = cont + 1
        while parar not in 'SN':
            parar = input('Deseja parar [S/N]: ').strip().upper()[0]
        if parar == 'S':
            print(f'O maior valor foi de {maior}') 
            break


lista()