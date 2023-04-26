x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
z = int(input('Digite o terceiro numero: '))
w = int(input('Digite o quarto numero: '))

tupla = (x, y, z, w)

achar = tupla.index(3)
cont9 = tupla.count(9)
contpar = 0

for num in tupla:
    if num % 2 == 0:
        contpar += 1

print(f'O numero 9 aparece {cont9} vezes')
print(f'O primeiro numero 3 foi digitado na posição: {achar+1}')
print(f'Voce digitou {contpar} numeros pares')
