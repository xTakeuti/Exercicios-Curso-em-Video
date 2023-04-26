import random
maior = 0
menor = 11
tupla = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
print(f'{tupla}')
for c in tupla[0:]:
    if c < menor:
        menor = c
    if c > maior:
        maior = c
print(f'O menor numero é {menor}')
print(f'O maior numero é {maior}')