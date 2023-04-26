import random
ganhei = 0
while True:
    maquina = random.randint(0, 10)
    n1 = int(input('Digite um numero de 0 a 10: '))
    par = str(input('Escolha par ou impar: [P/I]')).upper()
    print(f'Voce jogou {n1} e o computador {maquina}. Total de {n1 + maquina}')
    if (n1 + maquina) % 2 == 0:
        print('O numero é par')
        if par == 'P':
            print('Você ganhou!')
            ganhei += 1
        else:
            break
    else:
        print('O numero é impar')
        if par == 'I':
            print('Você ganhou!')
            ganhei += 1
        else:
            break
print('Você perdeu!')
print(f'Você ganhou {ganhei} vezes seguidas')