# Escrever um programa que leia separadamente a quantidade de dias, horas, minutos e segundos do usuário. Calcular o total em segundos

dias = int(input('Digite a quantidade de dias: '))
hr_dia = dias * 24
hrs = int(input('Digite a quantidade de horas: '))
cvs_dias = hr_dia * 3600
min = int(input('Digite a quantidade de minutos: '))
cvs_min = min * 60
sgs = int(input("Digite a quantidade de segundos: "))
cvs_hrs = hrs * 3600
total = cvs_hrs + cvs_dias + cvs_min
print(f'{total}s')  
