dic = {}
dic['nome'] = input('Nome da pessoa: ')
dic['media'] = int(input('Media do aluno: '))
print(f'Nome do aluno é {dic["nome"]}')
print(f'A media do aluno é {dic["media"]}')
if dic['media'] >= 7:
    print('Aprovado')
if dic['media'] < 7 and dic['media'] >= 5:
    print('Recuperação')
if dic['media'] < 5:
    print('Reprovado')