'''
O Detran resolveu instalar um radar no caminho entre a sua casa e a sua faculdade com o objetivo de eliminar a
velocidade da via dos carros em uma determinada via.
Mas resolveram inovar e a velocidade da via pode ser alterada diariamente. Por exemplo, nos feriados, eles
geralmente colocam a velocidade máxima em 80 km/h. Já durante a semana, é comum que a velocidade máxima
seja de 60 km/h.

Para isso, placas digitais informam aos motoristas qual é a velocidade máxima naquele momento.
A tabela de penalizações para quem ultrapassar esse limite é:
    • Velocidade até 20% superior ao permitido: multa de R$ 85,13 e 4 pontos na carteira;
    • Velocidade maior que 20% e até 50% acima do permitido: multa de R$ 127,69 e 5 pontos na carteira;
    • Velocidade acima de 50% do permitido: multa de R$ 574, 62; 7 pontos na carteira, apreensão da carteira e
    suspensão do direito de dirigir.

Você irá receber a velocidade máxima da via, a velocidade do carro e deve calcular o valor da multa e quantos
pontos na carteira o motorista perdeu, caso ele tenha ultrapassado o limite.

Entrada:  Dois números reais, correspondendo à velocidade máxima da via e a velocidade do veículo.
Saída: Você deve imprimir duas linhas. A primeira contém o valor de multa e a segunda o número de pontos da carteira.
O valor da multa deve ser formatado com duas casas decimais.
'''

vel_max = float(input('Velocidade máxima da via: '))
vel_veiculo = float(input('Velocidade do veículo: '))

a = vel_veiculo - vel_max
pctg = (a * 100) / vel_max

if pctg <= 20:
    print('Você irá receber uma multa de R$: 85.13 \nperdeu 4 pontos na carteira.')
elif pctg >= 21 and pctg <=50:
    print('Você irá receber uma multa de R$: 127.69 \nperdeu 5 pontos na carteira.')
elif pctg > 51:
    print('Você irá receber uma multa de R$: 574.62 \nperdeu 7 pontos na carteira, apreensão da carteira e suspensão do direito de dirigir ')
else:
    print('Dirigiu entre o limite permitido.')