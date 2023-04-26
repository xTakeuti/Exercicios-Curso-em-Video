lista_a = []
lista_b = []
npessoas = 0
maiorpeso = 0
pessoamaior = []
menorpeso = float("inf")
pessoamenor = []

while True:
    nome = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa (em kg): '))
    lista_a.append(nome)
    lista_a.append(peso)
    lista_b.append(lista_a[:])
    lista_a.clear()
    npessoas += 1
    cont = input('Deseja continuar? S/N ').upper()
    if cont == 'N':
        break

for p in lista_b:
    if p[1] >= maiorpeso:
        if p[1] > maiorpeso:
            maiorpeso = p[1]
            pessoamaior.clear()  # Limpa a lista quando encontra um novo maior peso
        pessoamaior.append(p[0])
    if p[1] <= menorpeso:
        if p[1] < menorpeso:
            menorpeso = p[1]
            pessoamenor.clear()  # Limpa a lista quando encontra um novo menor peso
        pessoamenor.append(p[0])

print(f'Você cadastrou {npessoas} pessoas!')
print(f'A pessoa com maior peso tem {maiorpeso} kg e é(são) a(s) pessoa(s) {pessoamaior}')
print(f'A pessoa com menor peso tem {menorpeso} kg e é(são) a(s) pessoa(s) {pessoamenor}')
