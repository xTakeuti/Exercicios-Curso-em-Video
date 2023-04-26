import random
from prettytable import PrettyTable

jogadores = []
for n in range(4):
    d = {}
    d['jogador'] = f"Jogador {n + 1}"
    d['numero'] = random.randint(1,6)
    jogadores.append(d)

jogadores_ordenados = sorted(jogadores, key=lambda k: k['numero'], reverse=True)

tabela = PrettyTable()
tabela.field_names = ["Jogador", "Pontuação"]

for jogador in jogadores_ordenados:
    tabela.add_row([jogador['jogador'], jogador['numero']])

print(tabela)
