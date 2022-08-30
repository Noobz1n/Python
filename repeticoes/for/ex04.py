# Tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Você deseja a tabuada do numero: '))

for tabuada in range(0, 11):
    result = num * tabuada
    print(f"{num}x{tabuada} = {result}")