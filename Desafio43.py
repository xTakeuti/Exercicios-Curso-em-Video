peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura **2
print(f'O valor do seu imc é: {imc:.1f}')

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.5 < imc <= 25:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Sobrepeso')
else:
    print('Obesidade mórbida')