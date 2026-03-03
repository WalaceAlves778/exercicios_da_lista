def inverter ():
    num = int(input('digite um numero:'))
    inverter_inteiro = 0
    while num > 0:
     algarismo = num % 10
     inverter_inteiro = (inverter_inteiro * 10) + algarismo
     num = num //10
    print(inverter_inteiro)

inverter()