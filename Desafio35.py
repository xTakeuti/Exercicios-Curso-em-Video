m1 = float(input('Digite a primeira medida do triangulo: '))
m2 = float(input('Digite a segunda medida do triangulo: '))
m3 = float(input('Digite a terceira medida do triangulo: '))

if m1 < m2+m3 and m2 <m1+m3 and m3<m2+m1:
    print('Seu triangulo \33[1;32;46mpode\33[m ser formado')
else:
    print('Seu triangulo \33[30;41mnão\33[m pode ser formado')
