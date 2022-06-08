print(f'Qual sua altura em metros? (ex: 1.78)')
altura = float(input(f'R: '))

print(f'\nQual seu peso em kgs? (ex: 90.0)')
peso = float(input(f'R: '))

if altura < 1.20 and peso <= 60.0:
    print(f'Você está na classificação A')
elif altura < 1.20 and 60.0 < peso < 90.0:
    print(f'Você está na classificação D')
elif altura < 1.20 and peso >= 90.0:
    print(f'Você está na classificação G')
elif 1.20 <= altura <= 1.70 and peso <= 60.0:
    print(f'Você está na classificação B')
elif 1.20 <= altura <= 1.70 and 60.0 < peso < 90.0:
    print(f'Você está na classificação E')
elif 1.20 <= altura <= 1.70 and peso >= 90.0:
    print(f'Você está na classificação H')
elif altura > 1.70 and peso <= 60.0:
    print(f'Você está na classificação C')
elif altura > 1.70 and 60.0 < peso < 90.0:
    print(f'Você está na classificação F')
else:
    print(f'Você está na classificação I')
