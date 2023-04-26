lista = []
lista_2 = []
contagem = 0
for n in range(9):
    lista.append(int(input('Digite o numero da matrix: ')))
    contagem += 1
    if contagem > 2:
        lista_2.append(lista[:])
        lista.clear()
        contagem = 0
print(lista_2[0])
print(lista_2[1])
print(lista_2[2])