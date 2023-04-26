import math
a = int(input('Qual angulo você deseja calcular? '))
cos = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tang = math.tan(math.radians(a))
print(f'Seu seno sera {sen:.2f} seu cosseno sera {cos:.2f} e sua tangente sera {tang:.2f}')
