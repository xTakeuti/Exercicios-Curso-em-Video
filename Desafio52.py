n = int(input('Digite um numero: '))
divi = 0
for c in range (1,n+1):
    if n % c == 0:
        print('\33[34m', end=' ')
        divi += 1
    else:
        print('\33[33m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {n} foi divisivel {divi} vezes')
if divi <= 2:
    print('Seu numero é primo')
else:
    print('Seu numero não é primo')