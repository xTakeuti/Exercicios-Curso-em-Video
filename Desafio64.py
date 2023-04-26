n1 = 0
contador = 0
c = 0
while c != 999:
    c = int(input('Digite um numero (999 para parar): '))
    n1 = c + n1
    contador = contador + 1
print(f'A soma dos valores é {n1 - 999} e voce tentou {contador - 1} vezes')