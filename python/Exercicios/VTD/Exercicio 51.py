import math

print('Escreva suas coordenadas (Use X,X)')
resposta = str(input('\nR: '))

coordenadasxa = int(resposta[0:1])
coordenadasya = int(resposta[2:3])

coordenadasxb = 0
coordenadasyb = 0

resultado = math.sqrt(((coordenadasxa - coordenadasxb) ** 2) + ((coordenadasya - coordenadasyb) ** 2))

print(f'Sua distância será {resultado:.2f}')
