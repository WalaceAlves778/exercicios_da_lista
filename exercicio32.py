import math

def numero_primo (n) :
    if n < 2:
        return False
    for i in range (2 ,int(math.sqrt(n))):
      if n % i == 0 :
         return False
    return True 

numero = int(input ('digite um numero: '))
      
if numero_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")