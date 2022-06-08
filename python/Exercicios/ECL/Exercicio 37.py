
print(f'Digite em qual horário você chegou (use -> xx:xx)')
hora_chegada = str(input(f'R: '))

print(f'\nDigite a hora de sáida. (use -> xx:xx)')
hora_saida = str(input(f'R: '))

if int(hora_chegada[0:2]) > int(hora_saida[0:2]):

    diff = int(hora_chegada[0:2]) - int(hora_saida[0:2])

    horas_estacionada_hi_maior_hf = 24 - diff

    if int(hora_chegada[3:5]) > 0:

        horas_estacionada_hi_maior_hf = horas_estacionada_hi_maior_hf + 1

        if horas_estacionada_hi_maior_hf == 1 or horas_estacionada_hi_maior_hf == 2:
            pagar = horas_estacionada_hi_maior_hf * 1
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hi_maior_hf == 3 or horas_estacionada_hi_maior_hf == 4:
            pagar = horas_estacionada_hi_maior_hf * 1.40
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hi_maior_hf >= 5:
            pagar = horas_estacionada_hi_maior_hf * 2
            print(f'Você terá que pagar R${pagar:.2f}')
    else:
        if horas_estacionada_hi_maior_hf == 1 or horas_estacionada_hi_maior_hf == 2:
            pagar = horas_estacionada_hi_maior_hf * 1
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hi_maior_hf == 3 or horas_estacionada_hi_maior_hf == 4:
            pagar = horas_estacionada_hi_maior_hf * 1.40
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hi_maior_hf >= 5:
            pagar = horas_estacionada_hi_maior_hf * 2
            print(f'Você terá que pagar R${pagar:.2f}')
else:

    horas_estacionada_hf_maior_hi = int(hora_saida[0:2]) - int(hora_chegada[0:2])

    if int(hora_chegada[3:5]) > 0:

        horas_estacionada_hf_maior_hi = horas_estacionada_hf_maior_hi + 1

        if horas_estacionada_hf_maior_hi == 1 or horas_estacionada_hf_maior_hi == 2:
            pagar = horas_estacionada_hf_maior_hi * 1
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hf_maior_hi == 3 or horas_estacionada_hf_maior_hi == 4:
            pagar = horas_estacionada_hf_maior_hi * 1.40
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hf_maior_hi >= 5:
            pagar = horas_estacionada_hf_maior_hi * 2
            print(f'Você terá que pagar R${pagar:.2f}')
    else:
        if horas_estacionada_hf_maior_hi == 1 or horas_estacionada_hf_maior_hi == 2:
            pagar = horas_estacionada_hf_maior_hi * 1
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hf_maior_hi == 3 or horas_estacionada_hf_maior_hi == 4:
            pagar = horas_estacionada_hf_maior_hi * 1.40
            print(f'Você terá que pagar R${pagar:.2f}')

        elif horas_estacionada_hf_maior_hi >= 5:
            pagar = horas_estacionada_hf_maior_hi * 2
            print(f'Você terá que pagar R${pagar:.2f}')
