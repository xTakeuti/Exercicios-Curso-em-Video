v = float(input('Quantos km/h o seu carro estava? '))
m = (v-80)*7.00
if v > 80:
    print('Você foi multado, sinto muito')
    print(f'O Valor da sua multa sera: {m}')
else:
    print('Você não foi multado ufa!')
