def metade(p=0, format=False):
    res = p / 2
    return res if format is False else moeda(res)
    

def dobro(p=0, format=False):
    res = p * 2
    return res if format is False else moeda(res)

def aumento(p=0, qtd=0, format=False):
    res = p + (p * qtd / 100)
    return res if format is False else moeda(res)


def diminuir(p=0, qtd=0, format=False):
    res = p - (p * qtd / 100)
    return res if format is False else moeda(res)


def moeda(preco = 0, moeda = 'R$', format=False):
    return f"{moeda}{preco:.2f}".replace('.', ',')