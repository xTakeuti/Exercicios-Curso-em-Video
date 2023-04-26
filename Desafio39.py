import datetime
a = int(input('Qual seu ano de nascimento? '))
atual = datetime.date.today().year
if atual - a > 18:
    print(f'Ja passou o tempo do seu alistamento, passou faz {atual - a - 18} ano/anos')
elif atual - a < 18:
    print(f'Você ainda precisa se alistar, falta {a - atual + 18} ano/anos')
else:
    print('Esta na hora de se alistar')