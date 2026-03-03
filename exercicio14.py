numero = int(input('digite um numero '))

def fatorial(x):
    fatorial =1
    for i in range(2,x+1):
        fatorial = fatorial *i
    
    return fatorial

print (fatorial(numero)) 
 