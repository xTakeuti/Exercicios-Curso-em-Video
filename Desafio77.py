palavras = ('abacate', 'banana', 'cafe', 'doce', 'elefante', 'floresta', 'girassol', 'hotel', 'industria',
            'jardim', 'kiwi', 'limao', 'melancia', 'ninho', 'oliveira', 'pneu', 'quintal', 'restaurante', 'sabonete', 'tigre')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end=(' '))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')