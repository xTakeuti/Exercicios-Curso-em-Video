maior = 0
menor = float('inf')
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite o numero da posição {cont}:')))
    if lista[cont] > maior:
        maior = lista[cont]
    if lista[cont] < menor:
        menor = lista[cont]
pos_maior = []
for i in range(len(lista)):
    if lista[i] == maior:
        pos_maior.append(i)
pos_menor = []
for i in range(len(lista)):
    if lista[i] == menor:
        pos_menor.append(i)
print(f'Voce digitou os valores: {lista}')
print(f'O menor numero da lista é {menor} na posição {pos_menor}')
print(f'O maior numero da lista é {maior} na posição {pos_maior}')
