continuar = 'S'
lista =[]
listapar = []
listaimpar = []
while continuar == 'S':
    valor = (int(input('Digite um valor para colocar na lista: ')))
    lista.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    continuar = input('Quer continuar? (S/N) ').upper()
    if continuar not in 'SN':
        print('Digite um valor valido')
        continuar = 'S'
print(f'A lista ordenada é: {lista}')
print(f'A lista ordenada de pares é: {listapar}')
print(f'A lista ordenada de impares é: {listaimpar}')