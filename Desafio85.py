lista = []

for n in range(3):
    lista.append(int(input('Digite um numero para colocar na lista: ')))

pares = []
impares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números ímpares:", impares)
