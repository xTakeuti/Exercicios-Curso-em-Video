pessoa = {}
lista = []
continuar = ''
while continuar != 'N':
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    pessoa['sexo'] = input('Digite o sexo da pessoa: (F/M)').upper()
    if pessoa['sexo'] not in 'FM':
        print('Digite um sexo valido')
        pessoa['sexo'] = input('Digite o sexo da pessoa: (F/M)').upper()
    lista.append(pessoa.copy())
    continuar = input('Quer continuar? ').upper()
print(lista)
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
print(f'A media de idade é {sum([pessoa["idade"] for pessoa in lista]) / len(lista)}')
print(f'As mulheres cadastradas foram: ')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'])