f = str(input('Escreva uma frase para ver se ela é um palindromo:\n')).upper().replace(' ','')
f2 = f[::-1]
if f == f2:
    print('Sua frase é um palindromo')
else:
    print('Sua frase não é um palindromo')