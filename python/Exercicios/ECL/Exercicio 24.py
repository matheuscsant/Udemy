print(f'Qual o valor do seu produto?')
produto = float(input(f'R: '))

print(f'Para qual estado deseja enviar seu produto? (MG, SP, RJ e MS)')
destino = str(input(f'R: '))

MG = (produto * 0.07) + produto
SP = (produto * 0.12) + produto
RJ = (produto * 0.15) + produto
MS = (produto * 0.08) + produto

if destino == 'MG' or destino == 'mg':
    print(f'O valor do seu produto, será vendido por {MG:.2f}')
elif destino == 'SP' or destino == 'sp':
    print(f'O valor do seu produto, será vendido por {SP:.2f}')
elif destino == 'RJ' or destino == 'rj':
    print(f'O valor do seu produto, será vendido por {RJ:.2f}')
elif destino == 'MS' or destino == 'ms':
    print(f'O valor do seu produto, será vendido por {MS:.2f}')
else:
    print(f'Estado inválido, tente novamente.') 
