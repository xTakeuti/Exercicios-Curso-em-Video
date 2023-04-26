n1 = contador = media = maior = 0
r = 'S'
menor = 1000000000
while r != 'N':
    n1 = int(input('Digite um numero: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
    contador = contador + 1
    media = n1 + media
    if maior <= n1:
        maior = n1
    if menor >= n1:
        menor = n1
print(f'Voce tentou {contador} vezes e a media dos numeros é {media / contador:.2f}')
print(f'O maior numero foi {maior} e o menor é {menor}')
print('Fim')

