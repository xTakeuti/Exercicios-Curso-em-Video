valor = int(input('Qual o valor que voce deseja sacar? '))
cinquenta = vinte = dez = um = 0
while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    if valor < 50:
        break
while True:
    if valor >= 20:
        valor -= 20
        vinte += 1
    if valor < 20:
        break
while True:
    if valor >= 10:
        valor -= 10
        dez += 1
    if valor < 10:
        break
while True:
    if valor >= 1:
        valor -= 1
        um += 1
    if valor < 1:
        break
print(f'Voce sacou {cinquenta} notas de cinquenta')
print(f'Voce sacou {vinte} notas de vinte')
print(f'Voce sacou {dez} notas de dez')
print(f'Voce sacou {um} notas de um')