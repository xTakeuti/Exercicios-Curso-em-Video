import random
tentativa = 1
n = int(input('Tente adivinhar o numero que estou pensando de 0 a 5: '))
r = random.randint(0, 5)
while n != r:
    n = int(input('Não é este numero, tente outro: '))
    tentativa = tentativa+1
print('Voce acertou')
print(f'Seu numero de tentativas foi {tentativa}')