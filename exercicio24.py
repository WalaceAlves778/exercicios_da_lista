lista = []
def gerador_numeros ():
    for i in range (1,16):
        lista.append(i)

gerador_numeros()

maior = max (lista)
menor = min (lista)

print (f'A lista é: {lista} \nE o maior número é: {maior}'
    f'\nE o menor é: {menor}')