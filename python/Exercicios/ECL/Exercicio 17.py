print(f'\nInforme a base maior')
basemaior = float(input('R: '))

print(f'\nInforme a base menor')
basemenor = float(input('R: '))

print(f'\nInforme a altura')
altura = float(input('R: '))

if basemenor <= 0 or basemaior <= 0:
    print(f'Uma das bases é menor ou igual a zero, tente novamente.')
else:
    result = (basemaior + basemenor) * altura / 2
    print(f'A área do trapézio é de {result}')
