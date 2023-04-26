lista = []

for c in range(5):
    valor = (int(input('Digite um valor: ')))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        for j in range(len(lista)):
            if valor <= lista[j]:
                lista.insert(j, valor)
                break

print(f'A lista ordenada é: {lista}')
