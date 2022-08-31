# Dados de entrada altura e sexo de uma pessoa, construir um algoritmo que calcule o peso ideal, usando as seguintes formulas, homens: (72.7 * altura) - 58          mulher: (62.1 * altura) - 44.7

altura = float(input('Digite a sua altura: '))
sexo = (input('''[M] - Masculino
[F] - Feminino
Digite o seu sexo: ''')).upper()
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é: {peso_ideal:.1f}kg.')
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é: {peso_ideal:.1f}kg.')
else:
    print('Opção inválida! Tente novamente.')