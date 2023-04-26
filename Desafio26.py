n = input('Digite uma frase: ') .lower().strip()
frase = n.count('a')
ap = n.find('a')+1
au = n.rfind('a')+1
print(f'A letra A aparece : {frase}')
print(f'O primeiro A aparece na posição :{ap}')
print(f'O ultimo A aparece na posição:{au}')
