lista = []
listanota = []
continuar = ''
while True:
    lista.append(input('Nome: '))
    lista.append(int(input('Nota 1: ')))
    lista.append(int(input('Nota 2: ')))
    listanota.append(lista[:])
    lista.clear()
    continuar = input('Deseja continuar? S/N ').upper()
    if continuar == 'N':
        break
for nota in range(len(listanota)):
    print('Numero -- Nome -- Media')
    print(f'{nota} --- {listanota[nota][0]} --- {listanota[nota][1] * listanota[nota][2] / 2}')

mostra = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe) '))
if mostra == 999:
    exit()
print(f'As notas de {listanota[mostra][0]} foram {listanota[mostra][1], listanota[mostra][2]}')
