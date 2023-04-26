m1 = float(input('Digite a primeira medida do triangulo: '))
m2 = float(input('Digite a segunda medida do triangulo: '))
m3 = float(input('Digite a terceira medida do triangulo: '))

if m1 < m2+m3 and m2 <m1+m3 and m3<m2+m1:
    if m1 == m2 == m3:
        print('Seu triangulo é EQUILÁTERO: todos os lados iguais')
    elif m1 == m2 or m1 == m3 or m2 == m3:
        print('Seu triangulo é ISÓSCELES: dois lados iguais, um diferente')
    else:
        print('Seu triangulo é ESCALENO: todos os lados diferentes')
else:
    print('Seu triangulo \33[30;41mnão\33[m pode ser formado')
