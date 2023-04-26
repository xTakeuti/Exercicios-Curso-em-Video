n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
escolha = 0
while escolha != 5:
    escolha = int(input('Digite oque vc deseja fazer com esse numero.\n1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Trocar os numeros\n5 - Sair do programa\n'))
    if escolha == 1:
        print(f'o valor da somas é {n1+n2}\n')
    elif escolha == 2:
        print(f'o valor da multiplicação é {n1*n2}\n')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior numero é{n1}\n')
        else:
            print(f'O maior numero é {n2}\n')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro numero: \n'))
        n2 = int(input('Digite o segundo numero: \n'))
print('Xau')
