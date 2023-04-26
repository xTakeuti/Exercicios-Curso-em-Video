idadecont = masculino = feminino = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: [F/M] ')).upper()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if idade > 17:
        idadecont += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
            feminino += 1
    if continuar == 'N':
        break

print(f'{idadecont} pessoas são maiores de 18')
print(f'{masculino} pessoas são homens')
print(f'{feminino} pessoas são mulheres com 20 anos ou menos')
print('Fim')
