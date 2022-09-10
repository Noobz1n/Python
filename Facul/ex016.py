'''
A regra de desconto é bem simples: se a quantidade de produtos comprados for igual ou maior que quinze, então o
desconto é concedido. O desconto também é concedido caso o valor total da compra seja maior ou igual a 40 reais.
O valor do desconto é de 15%.
Sua missão é fazer um programa que leia o código do produto, a quantidade comprada e imprima o valor que o
cliente deve pagar, já considerando o desconto quando aplicável.
Considere que o cliente só pode comprar um único tipo produto cada vez que usar o seu software

CODIGO:
1 = 5,30
2 = 6,00
3 = 3,20
4 = 2,50

'''

cod = int(input('Digite o código do produto: '))
qntdd = int(input('Digite a quantidade comprada: '))

if cod == 1:
    total = qntdd * 5.30
    if qntdd >= 15 and total >= 40:
        desconto = total * (15 / 100)
        print(f'O total a pagar com o desconto será de R$: {total - desconto:.2f}')
    else:
        print(f'O total a pagar será de R$: {total:.2f}')
elif cod == 2:
    total = qntdd * 6
    if qntdd >= 15 and total >= 40:
        desconto = total * (15 / 100)
        print(f'O total a pagar com o desconto será de R$: {total - desconto:.2f}')
    else:
        print(f'O total a pagar será de R$: {total:.2f}')
elif cod == 3:
    total = qntdd * 3.20
    if qntdd >= 15 and total >= 40:
        desconto = total * (15 / 100)
        print(f'O total a pagar com o desconto será de R$: {total - desconto:.2f}')
    else:
        print(f'O total a pagar será de R$: {total:.2f}')
elif cod == 4:
    total = qntdd * 2.50
    if qntdd >= 15 and total >= 40:
        desconto = total * (15 / 100)
        print(f'O total a pagar com o desconto será de R$: {total - desconto:.2f}')
    else:
        print(f'O total a pagar será de R$: {total:.2f}')
else:
    print('Código digitado errado, digite novamente!  [1-4]')