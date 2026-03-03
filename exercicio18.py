numeros_soma = []

def entrada_dados ():
   while True:
      numeros = int(input('digite um numero:'))
      if numeros != 0:
       numeros_soma.append(numeros)
       print (numeros_soma)
      else:      
       print (sum(numeros_soma))
       break
          

    

  
   

entrada_dados()