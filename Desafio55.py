menor = 0
maior = 0
for p in range(1,6):
    peso =float(input(f'Digite o peso da pessoa {p}: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor peso é {menor}')