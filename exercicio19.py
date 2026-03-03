lista_numeros=[] 
lista_numeros_pares=[]
lista_numeros_impares=[]
def gerador_numeros ():
    for i in range (1,51):
        lista_numeros.append(i)
def separador ():
    for num in lista_numeros:
       if num % 2 == 0:
        lista_numeros_pares.append(num)
    print (lista_numeros_pares)
gerador_numeros ()
separador ()