lista = []
lista_2 = []
contagem = somapar = soma_ter = maior_seg = 0
for n in range(9):
    numero = (int(input('Digite o numero da matrix: ')))
    lista.append(numero)
    contagem += 1
    if contagem == 2:
        if numero > maior_seg:
            maior_seg = numero
    if numero % 2 == 0:
        somapar += numero
    if contagem == 3:
        soma_ter += numero
    if contagem > 2:
        lista_2.append(lista[:])
        lista.clear()
        contagem = 0
print(lista_2[0])
print(lista_2[1])
print(lista_2[2])
print(f'A soma dos numeros pares é {somapar}')
print(f'A soma da terceira coluna é {soma_ter}')
print(f'O maior numero da segunda coluna é {maior_seg}')