jogador = {}
gols = []
jogador['nome'] = input('Qual nome do jogador? ')
qtdpartidas = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))

for n in range(qtdpartidas):
    gols.append(int(input(f'Quantos gols na partida {n} o jogador fez? ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)
print('='*25)
print(jogador)
print('='*25)
print(f'O campo nome tem o valor: {jogador["nome"]}')
print(f'O campo gols tem o valor: {jogador["gols"]}')
print(f'O campo total tem o valor {jogador["total"]}')
print('='*25)
print(f'O jogador {jogador["nome"]} jogou {qtdpartidas} partidas')
for n in range(qtdpartidas):
    print(f'Na partida {n}, fez {jogador["gols"][n]}')
print(f'Foi um total de {jogador["total"]} gols')