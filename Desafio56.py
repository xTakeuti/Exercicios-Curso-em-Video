p = int(input('Quantas pessoas são? '))
idade = 0
maior = 0
velho = str('')
mulher = 0
for i in range(1,p+1):
    print(f'--------- Pessoa {i} ---------')
    nome = str(input('Qual o nome? '))
    idades = int(input('Qual a idade? '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    idade += idades
    if idades > maior and sexo == 'M':
            maior = idades
            velho = nome
    if sexo == 'F' and idades < 21:
        mulher += 1
if velho == '':
    print('Você não cadastrou homens')
else:
    print(f'O homem mais velho é o {velho}')
print(f'A media de idade das pessoas citadas é {idade/p:.2f}')
print(f'Existem {mulher} mulheres com menos de 20 anos')
