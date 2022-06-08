
hora = str(input(f'\nQual a horário atual? (use xx:xx:xx)'))
duracao = int(input(f'\nQual a duração do experimento'))

horadig = hora[0:1]
minutodig = hora[3:5]
segdig = hora[6:8]

if duracao > 60:
    
    horas = duracao / 3600
    minutos = (duracao % 3600) / 60
    segrest = (duracao % 3600) * horas - 60 * minutos
    print(f'O experimento terminou as {horas}:{minutos}:{segrest}')

    if minutodig > 60 and segdig > 60:
        newHrs = horadig + 1
        newmins = minutodig + 1
        segdig = 0

        print(f'O experimento terminou as {newHrs + horas}:{newmins + minutodig}:{segdig + segrest}')
else:
    
    horas = duracao / 3600
    minutos = (duracao % 3600) / 60
    segrest = (duracao % 3600) * horas - 60 * minutos
    print(f'O experimento terminou as {horas}:{minutos}:{segrest}')
    