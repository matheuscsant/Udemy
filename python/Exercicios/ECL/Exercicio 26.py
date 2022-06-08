print(f'Qual Kms o carro percorreu?')
kilometros = float(input(f'R: '))

print(f'\nQuantos litros o carro consumiu?')
litros = float(input(f'R: '))

km_Litros = kilometros / litros
print(km_Litros)
if km_Litros < 8:
    print(f'Venda o seu carro, consome muito e anda pouco.')
elif 8 < km_Litros > 11:
    print(f'Seu carro é econômico.')
elif km_Litros > 12:
    print(f'Seu carro é super econômico.')
