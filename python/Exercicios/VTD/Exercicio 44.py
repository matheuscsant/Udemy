print(f'Qual a altura do degrau? (Em centímetros)')
degrau = float(input('R: '))

print(f'Qual a altura que deseja alcançar? (Em metros)')
alturaDes = float(input('R: '))

alturadegrau = degrau / 100

alturatotal = alturaDes / alturadegrau

print(f'Você terá que subir {int(alturatotal)} degraus')
