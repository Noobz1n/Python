'''galera = [['Victor', 18], ['Sylvia', 15], ['Gaspar', 3], ['Arrascaeta', 28]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''


galera = []
dados = []
maior = menor = 0


for c in range(0,3):
    dados.append(input('Digite o seu nome: '))
    dados.append(int(input('Digite a sua idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior+=1
    else:
        print(f'{p[0]} é menor de idade.')
        menor+=1
