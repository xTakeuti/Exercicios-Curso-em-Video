from Desafio107b import aumentar, diminuir, dobro, metade


p = float(input('Digite o preço: '))
print(f'A metade de {p} é {metade(p)}')
print(f'Aumentando 10% , temos {aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {diminuir(p, 13)}')
print(f'O dobro de {p} é: {dobro(p)}')