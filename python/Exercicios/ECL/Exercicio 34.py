print(f'Digite sua nota')
nota = float(input(f'R: '))

print(f'\nDigite quantas faltas você teve')
faltas = int(input(f'R: '))

if 9.0 <= nota <= 10 and faltas <= 20:
    print(f'Seu conceito foi: A')
elif 7.5 <= nota <= 8.9 and faltas <= 20 or 9.0 <= nota <= 10 and faltas > 20:
    print(f'Seu conceito foi: B')
elif 5.0 <= nota <= 7.4 and faltas <= 20 or 7.5 <= nota <= 8.9 and faltas > 20:
    print(f'Seu conceito foi: C')
elif 4.0 <= nota <= 4.9 and faltas <= 20 or 5.0 <= nota <= 7.4 and faltas > 20:
    print(f'Seu conceito foi: D')
elif 0.0 <= nota <= 3.9 and faltas <= 20 or 4.0 <= nota <= 4.9 and faltas > 20 or 0.0 <= nota <= 3.9 and faltas > 20:
    print(f'Seu conceito foi: E')
