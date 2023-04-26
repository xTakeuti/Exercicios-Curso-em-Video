def jogador():
    x = input('Nome do jogador: ')
    if x == '':
        x = 'Desconhecido'
    y = input('Numero de gols: ')
    if y == '':
        y = 0
    else:
        y = int(y)
    print(f'O jogador {x} fez {y} gols no campeonato')

jogador()
