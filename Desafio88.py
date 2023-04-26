import random
lista = []
lista2 = []
nsorteios = int(input('Quantos jogos voce deseja? '))

for c in range(nsorteios):
    lista.append(random.randint(0, 99))
    lista.append(random.randint(0, 99))
    lista.append(random.randint(0, 99))
    lista.append(random.randint(0, 99))
    lista.append(random.randint(0, 99))
    lista.append(random.randint(0, 99))
    lista2.append(lista[:])
    lista.clear()
for n in range(len(lista2)):
    print(f'Jogo {n+1}: {lista2[n]}')