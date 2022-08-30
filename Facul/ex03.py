# calcular o aumento do salário. deve solicitar o valor do salário e a porcentagem do aumento. exibir o valor do aumento e do novo salário

salario = float(input("Digite o seu salário atual: "))
pctg_aumento = int(input('Digite a porcentagem do aumento: '))
val_aumento = (pctg_aumento / 100) * salario
salario_novo = salario + val_aumento
print(f'O seu aumento foi de: R$: {val_aumento}')
print(f'Seu salário irá de {salario} para {salario_novo}')