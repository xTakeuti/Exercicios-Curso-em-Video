cont = n2 = 0

while True:
    n1 = int(input('Digite um numero: '))
    if n1 == 999:
        break
    cont += 1
    n2 = n1 + n2
print(f'O valor de {cont} numeros somados serão {n2}')