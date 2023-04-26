import math
o = float(input('Digite o tamanho do cateto oposto: '))
a = float(input('Digite o tamanho do cateto adjacente: '))

print(f'O tamanho da sua hipotenusa sera de {math.sqrt(o*o+a*a):.2f}')
