print(f'\nQual seu sexo? (responda com F para feminino e M para masculino).')
sexo = str(input(f'\nR: '))

print(f'\nQual sua altura? (Em metros, por exemplo 1.78).')
altura = float(input(f'\nR: '))

if sexo == ('F') or ('f'):
    peso = (62.1 * altura) - 44.7
    print(f'\nSeu peso ideal é {peso} Kgs.')
else:
    peso = (72.7 * altura) - 58
    print(f'\nSeu peso ideal é {peso} Kgs.')
