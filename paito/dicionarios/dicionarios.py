import os
os.system('cls')






dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])


# Adicionar elementos no dicionario
dados['sexo'] = 'M'
print(dados['sexo'])

# Remover elementos
del dados['nome']

# Valores, items e keys.        items é tudo, keys é a palavra principal (titulos) e valores são os depois do :
filmes = {
    'Titulo': 'Star Wars',
    'Ano': 1977,
    'diretor': 'Jorge Lucas'
}
print(filmes)


# Laço de repetição
for k, v in filmes.items():
    print(f'O {k} é {v}')


# Adicionando itens no dicionario dentro de uma lista
brasil = []
estado = {}

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)