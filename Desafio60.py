n1 = int(input('Digite um numero para saber seu fatorial: '))
fatorial = n1 - 1
while fatorial != 0:
    n1 = fatorial * n1
    fatorial = fatorial - 1
print(f'Seu numero faturado é {n1}')