import os
os.system('cls')





''' 
num = [2, 5, 9, 1]
num[2] = 3  # Substitui o número do índice 2 por o valor 3
num.append(7) # Adiciona o 7 ao final da lista
num.sort() # Ordena a lista na ordem crescente
num.sort(reverse=True) # Ordena a lista na ordem decrescente
print(num)
num.insert(2, 2) # Vai inserior o número 0 depois do índice 2
print(num)
# num.pop(2) Vai eliminar o número do indice 2
if 5 in num:           # Se 5 estiver na lista (num)
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')
'''


valores = []
# valores.append(2)
# valores.append(14)
# valores.append(10)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(cont)
print(valores)
for c, v in enumerate(valores):
    print(f'No índice {c}, tem o valor: {v}.')



a = [14, 15, 18]
b = a[:] # Aqui ele vai copiar a lista de A pra B, e não vai fazer uma ligação