total = valorcont = 0
barato = 10000000000000
nomebarato = 'Nada'
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    total += valor
    if valor >= 1000:
        valorcont += 1
    if valor < barato:
        barato = valor
        nomebarato = nome
    if continuar == 'N':
            break
print(f'Temos {valorcont} produtos que custam mais de 1000')
print(f'O total da compra foi {total}')
print(f'o produto mais barato é {nomebarato} que custa {barato}')