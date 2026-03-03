lista = []
quadrado = []
def gerador_numeros ():
    for i in range (1,11):
        lista.append(i)

def lista_ao_quadrado ():
    for item in lista :
     resultado = item  ** 2
     quadrado.append(resultado)
    print (f'Lista original: {lista} \nLista com os valores ao '
           f'quadrado : {quadrado} ')

gerador_numeros ()
lista_ao_quadrado ()