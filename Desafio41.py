import datetime
ano = int(input('Digite o ano que o atleta nasceu para saber sua categoria?'))
idade = datetime.date.today().year - ano
if idade < 10:
    print('Mirim')
elif 9 < idade < 15:
    print('Infantil')
elif 14 < idade < 20:
    print('Junior')
elif 19 < idade < 21:
    print('Senior')
else:
    print('Master')
