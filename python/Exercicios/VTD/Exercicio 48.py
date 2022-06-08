print(f'\nQual o valor em segundos que você deseja converter?')
segundos = int(input('\nR: '))

Horas = segundos / 3600
minutos = (segundos % 3600) / 60
restosegundos = segundos % 3600 * Horas - 60 * minutos

print(f'Você deu {segundos} segundos, logo você terá {Horas:.2f} Hrs, {minutos:.2f} mnts e {restosegundos:.2f} segundos')
