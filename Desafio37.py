n = int(input('Escolha um numero: '))
m = int(input('Digite o numero referente ao que você quer transformar seu numero \n1 - Binario \n2 - Octal \n3 - Hexadecimal\n'))
if m == 1:
    print(f'Em binario seu numero ficara {bin(n)}')
elif m == 2:
    print(f'Em octal seu numero ficara {oct(n)}')
elif m == 3:
    print(f'Em Hexadecimal seu numero ficara {hex(n)}')
else:
    print('Essa opção não existe.')
