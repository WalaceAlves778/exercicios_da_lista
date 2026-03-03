peso = float(input('digite seu peso:'))
altura= float(input('digite sua altura:'))

imc = peso / (altura * altura)
 
print (f'seu imc é de:{imc:.2f}kg/m')