jogadores = []
continuar = 'S'

while continuar == 'S':
    jogador = {}
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    jogador['gols'] = []
    for n in range(jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {n+1} o jogador fez? ')))
    jogadores.append(jogador)
    continuar = input('Quer continuar (S/N): ').upper()

for jogador in jogadores:
    print('-'*50)
    print(f'Jogador: {jogador["nome"]}')
    print(f'Gols: {jogador["gols"]}')
    print(f'Total de gols: {sum(jogador["gols"])}')
