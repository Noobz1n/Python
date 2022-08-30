# Calcular a redução do tempo de vida de um fumante, pergunte  a quantidade de cigarros fumados no dia e qnts anos ele já fumou. Fumante perde 10min de vida por cigarro. Calcular quantos dias de vida o fumante perderá. Exibir o total em dias

cigarros = int(input('Quantos cigarros você fuma ao dia: '))
cigarros_hoje = int(input('Quantos você já fumou hoje: '))
anos = int(input('Quantos anos você fuma: '))
dias_ano = anos * 365
min_anos = dias_ano * 10
min_cigarros = cigarros * 10
min_hoje = cigarros_hoje * 10
dias = (min_anos + min_cigarros + min_hoje) / 1440
print(f'Você perdeu {dias:.4f} dias de vida')