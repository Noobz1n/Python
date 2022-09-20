'''Faça um programa que leia números inteiros até que o usuário digite 0. No final exiba a quantidade de números digitados, assim como a soma destes números e a média aritmética.'''


contador=1
numerointeiro=0
informador=0


while (contador > 0):
    informador = int(input("Informe um numero inteiro: "))
    numerointeiro = numerointeiro + informador
    contador = contador + 1
    print("Caso você não queira continuar adicionando mais numeros inteiros, digite 0 para finaliza o programa.")
    if (informador == 0):
        contador = contador - 2
        total = numerointeiro / contador
        print(f'Você digitou um total de {contador} vezes.')
        print(f'A média aritmética dos numéros é: {total}')
        contador=0