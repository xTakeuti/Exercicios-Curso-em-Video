def leiaint():
    m = input('Digite um numero: ')
    if m.isdigit():
        return int(m)
    else:
        print('Erro: não foi digitado um número inteiro')

n = leiaint()
if n != None:
    print(f'Voce digitou o numero: {n}')