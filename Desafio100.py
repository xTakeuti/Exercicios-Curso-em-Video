import random
lista = []
def sorteio():
    for n in range(5):
        lista.append(random.randint(1,9))
    print(f'Sorteando 5 valores : {lista}')
def pares(*soma):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteio()
pares()