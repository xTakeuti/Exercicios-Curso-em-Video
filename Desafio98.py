def contagem(x,y,z):
    print(f'Contagem de {x} até {y} de {z} em {z}')
    if x > y:
        z = -z
    for n in range(x,y+1,z):
        print(n,end=' ')
    print('\n')


contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(x=int(input('Inicio: ')),y=int(input('Fim: ')),z=int(input('Passo: ')))