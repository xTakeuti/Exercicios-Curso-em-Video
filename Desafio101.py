import datetime
def voto(y):
    idade = datetime.datetime.now().year - y
    if idade >= 18 and idade <= 70:
        print('VOTO OBRIGATORIO')
    elif idade <18 and idade >=16 or idade > 70:
        print('VOTO OPCIONAL')
    else:
        print('VOTO NEGADO')


voto(int(input('Digite o seu ano de nascimento: ')))