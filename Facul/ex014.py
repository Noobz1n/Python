'''
Solicitaram que você faça um update no programa do exercício 3. Após exibir a multa, deverá solicitar o valor da cotação do dólar
e imprimir na tela os valores em dólar e em real.
1 DOLAR = R$: 5.16    05/09/2022
'''

gasto = int(input('Digite o total gasto na viagem ($): '))
if gasto > 500:
    resto = gasto - 500
    print('Você excedeu o limite de 500 dólares, deve pagar uma imposto de 50%.')
    print(f'Você ultrapassou $: {resto}.')
    print(f'Você ultrapassou R$: {resto * 5.16}.') #Conversão direta, sem criar variavel
    imposto = resto * (50 / 100)
    print(f'O imposto de 50% em cima dos $: {resto}, será de: $: {imposto}')
    print(f'O imposto de 50% em cima dos R$: {resto * 5.16}, será de: R$: {imposto * 5.16}')
else:
    print('Parabéns, você não pagará imposto!')
    