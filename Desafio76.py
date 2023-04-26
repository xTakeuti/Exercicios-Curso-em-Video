tupla = ('queijo', 2.00, 'leite', 4.50, 'pao', 0.50)

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end= ' ')
    else:
        print(f'R${tupla[pos]:>5.2f}')