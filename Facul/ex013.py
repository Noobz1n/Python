''' 
Ao viajar para o exterior , uma pessoa pode trazer no máximo 500 dólares em compras. Se o valor ultrapassar 500, ela deve
pagar um imposto de 50% do valor que exceder os 500 dólares. Por exemplo, se um passageiro gastou 820 dólares, ele ultrapassou
o limite em 320 dólares, logo, o imposto será de 50% em cima dos 320, ou seja, 160 dólares


Faça um programa que receba o total
gasto por um viajante e imprime o valor total a ser pago de imposto. Perceba que se o valor da compra for igual ou menor que 500,
o valor do imposto será 0.'''

gasto = int(input('Digite o total gasto na viagem: '))

if gasto > 500:
    resto = gasto - 500
    print('Você excedeu o limite de 500 dólares, deve pagar uma imposto de 50%.')
    print(f'Você ultrapassou $: {resto}.')
    imposto = resto * (50 / 100)
    print(f'O imposto de 50% em cima dos $: {resto}, será de: $: {imposto}')
else:
    print('Parabéns, você não pagará imposto!')