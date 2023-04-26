primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' ')
        termo += razao
        cont += 1
    print('PAUSA\n')
    mais = int(input(f'Quantos termos mais voce deseja ver?'))
print('FIM')