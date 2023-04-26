def notas(*ava, sit=False):
    nota = {}
    total = 0
    for n in ava:
        nota[f'nota{n}'] = n
        total += n
    media = total / len(ava)
    nota['media'] = media
    print(f'Total: {len(ava)}')
    print(f'Media: {media}')
    return nota

notas(1,2,3,4)
