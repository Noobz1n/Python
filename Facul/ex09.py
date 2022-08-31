# Ler tres valores diferentes e mostre em ordem decrescente, utilizando uma selecao encadeada

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = int(input('Digite n3: '))
if (n1 > n2 > n3):
    print(f'{n1}, {n2} e {n3}')
elif (n1 > n3 > n2):
    print(f'{n1}, {n3} e {n2}')
elif (n2 > n1 > n3):
    print(f'{n2}, {n1} e {n3}')
elif (n2 > n3 > n1):
    print(f'{n2}, {n3} e {n1}')
elif (n3 > n1 > n2):
    print(f'{n3}, {n1} e {n2}')
else:
    print(f'{n3}, {n2} e {n1}')