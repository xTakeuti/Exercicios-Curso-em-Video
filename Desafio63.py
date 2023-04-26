n1 = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print(t1 + t2, end=' ')
while n1 != 0:
    t3 = t1 + t2
    print(t3, end=' ')
    n1 = n1 - 1
    t1 = t2
    t2 = t3
print('Fim')