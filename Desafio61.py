primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += razao
    cont += 1
print('FIM')