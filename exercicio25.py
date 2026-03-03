import random
lista = []
for numeros in range (10):
    numeros = (random.randint(1,100))
    lista.append(numeros)
print(f'lista gerada aleatoriamente: {lista}')
lista.sort ()
print (f'lista ordenada de forma crescente: {lista}')