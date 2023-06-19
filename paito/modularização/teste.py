'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moedas
import os
os.system('cls')



p = float(input('Digite o preço: R$'))
print(f'A metade do preco de R${p:.2f} é {moedas.metade(p)}')
print(f'O dobro do preco de R${p:.2f} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumento(p, 10)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13)}')






'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''
print('''
OUTRO EXERCICIO
''')
print(f'A metade do preco de {moedas.moeda(p, "R$")} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro do preco de {moedas.moeda(p, "R$")} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumento(p, 10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}')




'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
print('''
OUTRO EXERCICIO
''')
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumetando 10%, temos {moedas.aumento(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}')
