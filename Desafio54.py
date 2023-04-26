from datetime import date

atual = date.today().year
tmaior = 0
tmenor = 0
for i in range(0,7):
    nasc = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    idade = atual - nasc

    if idade >= 18:
        tmaior += 1
    else:
        tmenor += 1
print(f'Exitem {tmaior} maior de idade e {tmenor} menor de idade')