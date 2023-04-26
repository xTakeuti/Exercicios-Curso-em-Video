numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if escolha < 20 and escolha > 0:
        break
    else:
        print('Numero invalido')
print(f'Você digitou o numero {numero[escolha]}')