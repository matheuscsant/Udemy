
print(f'Diga sua data de nascimento')

print(f'\nDiga em qual dia você nasceu')
dianas = int(input(f'R: '))

print(f'\nDiga em qual mês você nasceu')
mesnas = int(input(f'R: '))

print(f'\nDiga em qual ano você nasceu')
anonas = int(input(f'R: '))

anobissexto = anonas % 4

if anobissexto == 0 and anonas < 2021:    
    
    if 0 < mesnas > 13:
        
        if mesnas == 2 and dianas <= 29:
            print(f'\nData válida')
        
        elif mesnas == 4 or 6 or 9 or 11 and dianas <= 30:
            print(f'\nData válida')
        
        elif mesnas == 1 or 3 or 5 or 7 or 8 or 10 or 12 and dianas <= 31:
            print(f'\nData válida.')

elif anobissexto <=1 and anonas < 2021:
        
        if mesnas == 2 and dianas <= 28:
            print(f'\nData válida')
        
        elif mesnas == 4 or 6 or 9 or 11 and dianas <= 30:
            print(f'\nData válida')
        
        elif mesnas == 1 or 3 or 5 or 7 or 8 or 10 or 12 and dianas <= 31:
            print(f'\nData válida.')

else:
    print(f'\nData inválida.')