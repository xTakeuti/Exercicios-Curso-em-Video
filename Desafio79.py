continuar = 'S'
lista =[]
while continuar == 'S':
    lista.append(int(input('Digite um valor para colocar na lista: ')))
    continuar = input('Quer continuar? (S/N) ').upper()
    if continuar not in 'SN':
        print('Digite um valor valido')
        continuar = 'S'
lista.sort()
print(lista)