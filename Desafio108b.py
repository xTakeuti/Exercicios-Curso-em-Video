def aumentar(p, x):
    k = p+(p/100*x)
    return k
def dobro(p):
    k = p*2
    return k
def metade(p):
    k = p/2
    return k
def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')