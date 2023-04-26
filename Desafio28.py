import random

n = int(input('Tente adivinhar o numero que estou pensando de 0 a 5: '))
r = random.randint(0, 5)
if r == n:
    print(f'Acertou mizeravi o numero é {r}')
else:
    print(f'O numero era {r}, mas tente denovo')
