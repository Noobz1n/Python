#solicite o preço de uma mercadoria e o percentual de desconto. exiba o valor do desconto e o preço a pagar

preco = float(input("Valor sem desconto: "))
desconto = int(input("Porcentagem do desconto (%): "))
valor_descontado = preco * (desconto / 100)
valor_final = preco - valor_descontado
print(f'O desconto foi de: {valor_descontado}')
print(f'Você irá pagar {valor_final} já com o desconto.')
