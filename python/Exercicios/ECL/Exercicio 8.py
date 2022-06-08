print(f'\nDigite a nota do primeiro bimestre.')
bim1 = float(input(f'\nR: '))

print(f'\nDigite a nota do segundo bimestre.')
bim2 = float(input(f'\nR: '))

if 0 <= bim1 and bim2 < 10:
    print(f'\nSua média é {(bim1 + bim2) / 2}.\n')
else:
    print(f'\nNotas inválidas, execute novamente.\n')
