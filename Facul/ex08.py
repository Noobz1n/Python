# Determinar o numero de dias que a pessoa já viveu, o usuario deve informar a data de nascimento ea data atual. mes 30 dias e ano 365. variavel pro dia, mes e ano
print('-'*100)
dia_nasc = int(input('Digite o dia do seu nascimento: '))
mes_nasc = int(input('Digite o mês do seu nascimento: '))
ano_nasc = int(input('Digite o ano do seu nascimento: '))
print('-'*100)
dia_atual = int(input('Digite o dia atual: '))
mes_atual = int(input('Digite o mês atual: '))
ano_atual = int(input('Digite o ano atual: '))
print('-'*100)
ctg_ano = ano_atual - ano_nasc
ctg_ano = ctg_ano * 365
ctg_mes = mes_atual - mes_nasc
ctg_mes = ctg_mes * 30
total = (dia_nasc + dia_atual) + ctg_ano + ctg_mes
print(f'{total} dias.')