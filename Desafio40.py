n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('APROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
