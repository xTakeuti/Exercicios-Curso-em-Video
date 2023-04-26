continuar = 'S'
lista =[]
cont = 0
while continuar == 'S':
    lista.append(int(input('Digite um valor para colocar na lista: ')))
    continuar = input('Quer continuar? (S/N) ').upper()
    cont += 1
    if continuar not in 'SN':
        print('Digite um valor valido')
        continuar = 'S'
lista.sort(reverse=True)
print(f'Voce digitou {cont} valores')
print(f'A lista em seu valor decrecente é {lista}')
if 5 in lista:
    print('Sua lista tem 5')
else:
    print('Sua lista nao tem 5')