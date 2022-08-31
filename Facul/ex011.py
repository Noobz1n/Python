''' alcular imc = peso / altura**2 , elaborar um algoritmo de um adulto e mostre a condicao: 
abaixo de 18,5 = abaixo do peso
entre 18,5 = peso normal
entre 25 e 30 = acima do peso
acima de 30 = obeso
'''
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2
if imc == 18.5:
    print(f'Seu imc é: {imc:.1f}. Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu imc é: {imc:.1f}. Você está com o peso normal.')
elif imc >= 25 and imc <= 30:
    print(f'Seu imc é: {imc:.1f}. Você está acima do peso.')
else:
    print(f'Seu imc é: {imc:.1f}. Você está obeso.')