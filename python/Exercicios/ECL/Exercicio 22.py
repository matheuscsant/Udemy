print(f'Digite sua idade.')
idade = int(input('R: '))

print(f'\nDigite quantos anos você já trabalhou.')
anos_trabalhados = int(input('R: '))

if idade == 65:
    print(f'\nVocê pode se aposentar.')
elif anos_trabalhados == 30:
    print(f'\nVocê pode se aposentar.')
elif idade == 60 and anos_trabalhados == 25:
    print(f'\nVocê pode se aposentar.')
else:
    print(f'Você não pode se aposentar.')
