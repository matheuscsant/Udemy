print(f'Digite sua idade')
idade = int(input(f'R: '))

if 5 <= idade <= 7:
    print(f'Você foi classificado como Infantil A')
elif 8 <= idade <= 10:
    print(f'Você foi classificado como Infantil B')
elif 11 <= idade <= 13:
    print(f'Você foi classificado como Juvenil A')
elif 14 <= idade <= 17:
    print(f'Você foi classificado como Juvenil B')
elif idade >= 18:
    print(f'Você foi classificado como Sênior')
else:
    print(f'Não é possível fazer a classificação')
