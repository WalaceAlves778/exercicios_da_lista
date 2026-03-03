lista = [1,1,2,2,5,5,4,4,7,7]
lista_unica = []
for numeros in lista:
    if numeros not in lista_unica:
        lista_unica.append(numeros)
print(lista_unica)
#not [] (lista vazia) retorna True, porque listas
#  vazias são "falsas".