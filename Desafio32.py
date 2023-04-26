import datetime
a = int(input('Digite um ano para saber se ele é bissexto: '))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    input(f'O ano {a} é bissexto')
else:
    input(f'O ano {a} não é bissexto')
