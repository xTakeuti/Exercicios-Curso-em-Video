s = float(input('Digite o seu salario para saber o aumento: '))
if s > 1250.00:
    print(f'Seu salario sera {s/100*110}')
else:
    print(f'Seu salario sera {s/100*115}')
