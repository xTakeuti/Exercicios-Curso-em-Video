expressao = input('Digite a expressão: ')
pilha = []

for caracter in expressao:
    if caracter == '(':
        pilha.append(caracter)
    elif caracter == ')':
        if len(pilha) > 0 and pilha[-1] == '(':
            pilha.pop()
        else:
            pilha.append(caracter)
            break

if len(pilha) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
