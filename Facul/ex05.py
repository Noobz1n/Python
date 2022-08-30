# Calcular o tempo de uma viagem de carro. Perguntar a distancia a percorrer e a velocidade media esparada para a viagem
lugar = input('Pra onde você vai?: ')
km = int(input('Distancia a percorrer: (km) '))
vel = int(input('Velocidade media esperada: (km/h '))
hr = km / vel
print(f'Para você ir a/ao {lugar} na distancia de {km}km e com a velocidade media de {vel}km/h, irá demorar {hr} hrs.')