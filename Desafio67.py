total = 0
while True:
    n = int(input('Digite um numero para ver a tabuada: '))
    if n <0:
        break
    for c in range(1,11):
        total = c * n
        print(f'{c} x {n} = {total} ')
print('O programa finalizou')