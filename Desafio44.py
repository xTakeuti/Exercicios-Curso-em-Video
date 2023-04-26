p = float(input('Qual o valor do produto? '))
tipo = input('Qual a forma de pagamento? \n1 - Dinheiro ou cheque (10% de desconto) \n2 - A vista no cartão (5% de desconto) \n3 - Até 2x no cartão (Valor normal) \n4 - 3x ou mais (20% de juros)\n')
if tipo == '1':
    print(f'O valor sera {p/100*90}')
elif tipo == '2':
    print(f'O valor sera {p/100*95}')
elif tipo == '3':
    print(f'O valor sera {p}')
elif tipo == '4':
    print(f'O valor sera {p/100*120}')
