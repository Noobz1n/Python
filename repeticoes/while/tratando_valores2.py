import os
os.system('cls ')








n = d = s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    d+=1
    if n == 999:
        break
    s = s + n
print(f'A soma dos {d} valores é igual a {s}')