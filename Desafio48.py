soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = c + soma
        print(c, end=' ')
print(f'\nA soma dos valores são: {soma}')