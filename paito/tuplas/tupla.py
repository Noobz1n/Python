import os
os.system('cls')



lanche = ('Strogonoff', 'Coca Cola', 'Brigadeiro', 'Pizza', 'Batata palha')
'''
print(lanche)
print(lanche[3])
print(lanche[-5])
'''


# Forma 1
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

# Forma 2
for comida in lanche:
    print(f'Irei comer {comida}')

# Forma 3 que da a posição do indice
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posicao {pos}')

# Forma 4 pra ordenar em ordem alfabetica  | transforma a tupla em lista.
print(sorted(lanche))


# Tupla com números
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b    #concatena a tupla A com a B sem alterar a ordem.
print(c)
print(c.count(5)) # vai mostrar quantas vezes aparece o número 5 na tupla da variavel c
print(c.index(8)) # vai mostrar a posição indice do número 8
print(c.index(5, 1)) # vai mostrar o indice do primeiro 5 que aparecer depois do indice 1