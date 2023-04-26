def maior(*num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print('Analisando valores passados...')
    print(f'{num} Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 5, 3, 9)
maior()