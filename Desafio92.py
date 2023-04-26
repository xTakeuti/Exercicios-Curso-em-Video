import datetime
trabalho = {}
trabalho['nome'] = input('Nome: ')
trabalho['nascimento'] = int(input('Ano de nascimento: '))
trabalho['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalho['carteira'] != 0 :
    trabalho['contratação'] = int(input('Ano de contratação: '))
    trabalho['salario'] = float(input('Salario: '))
print('='*25)
print(f'Nome: {trabalho["nome"]} ')
print(f'Idade: {datetime.datetime.now().year - trabalho["nascimento"]}')
print(f'Ctps: {trabalho["carteira"]}')
