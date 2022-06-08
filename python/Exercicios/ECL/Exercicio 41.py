

print(f'Para calcular seu IMC, será necessário o fornecimento de algumas informações como: peso e altura')
print(f'Qual sua altura em metros?')
altura = float(input(f'R: '))

print(f'Qual seu peso em Kgs?')
peso = float(input(f'R: '))

IMC = peso / altura ** 2

if IMC <= 18.5:
    print(f'Seu cálculo no IMC foi de: {IMC:.2f}Kg/m². Logo, você está abaixo do peso ideal.')
elif 16.8 <= IMC <= 24.9:
    print(f'Seu cálculo no IMC foi de: {IMC:.2f}Kg/m². Logo, você está saudável.')
elif 25.0 <= IMC <= 29.9:
    print(f'Seu cálculo no IMC foi de: {IMC:.2f}Kg/m². Logo, você está com peso em excesso.')
elif 30.0 <= IMC <= 34.9:
    print(f'Seu cálculo no IMC foi de: {IMC:.2f}Kg/m². Logo, você está com obesidade grau I.')
elif 35.0 <= IMC <= 39.9:
    print(f'Seu cálculo no IMC foi de: {IMC:.2f}Kg/m². Logo, você está com obesidade grau II.')
elif 40.0 <= IMC:
    print(f'Seu cálculo no IMC foi de: {IMC:.2f}Kg/m². Logo, você está com obesidade grau III.')
else:
    print(f'Cálculo inválido, por favor contatar o suporte.')