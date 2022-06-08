
print(f'\nDigite o valor do prêmio')
premio = float(input('\nR: '))

print(f'\nDigite quando o primeiro apostador apostou')
apostador1 = float(input('\nR: '))

print(f'\nDigite quando o segundo apostador apostou')
apostador2 = float(input('\nR: '))

print(f'\nDigite quando o terceiro apostador apostou')
apostador3 = float(input('\nR: '))

apostatotal = apostador1 + apostador2 + apostador3

perc_aposta1 = (apostador1 / apostatotal) * 100 #Pegando percentual
perc_aposta2 = (apostador2 / apostatotal) * 100 #Pegando percentual
perc_aposta3 = (apostador3 / apostatotal) * 100 #Pegando percentual

premio_primeiro_apostador = premio * (perc_aposta1 / 100)
premio_segundo_apostador = premio * (perc_aposta2 / 100)
premio_terceiro_apostador = premio * (perc_aposta3 / 100)

print(f'\nA porcentagem do primeiro apostador será {perc_aposta1}% e ele receberá {premio_primeiro_apostador}')
print(f'\nA porcentagem do segundo apostador será {perc_aposta2}% e ele receberá {premio_segundo_apostador}')
print(f'\nA porcetagem do terceiro apostador será {perc_aposta3}% e ele receberá {premio_terceiro_apostador}')
