import random
lista = []
for numeros in range (10):
    numeros = (random.randint(1,100))
    lista.append(numeros)
print(f'lista aleatoria: {lista}')

valor_total = (sum(lista))
print(f'a soma total da lista:{valor_total}')