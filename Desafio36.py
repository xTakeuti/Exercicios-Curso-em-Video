import playsound
casa = float(input('Qual o valor da casa? '))
s = float(input('Qual seu salario? '))
ano = int(input('Quantos anos voce vai pagar? '))
p = casa/(12*ano)
print(f'Sua prestação mensal ficara no valor de R${p:.2f}')
if p > s/100*130:
    print('Infelismente seu emprestimo foi negado')
else:
    print('Seu emprestimo foi aceito parabens')
    playsound.playsound('bape2.mp3')
