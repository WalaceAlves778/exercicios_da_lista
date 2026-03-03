def palindromo ():
    palavra = input ('digite uma palavra \nque seja um palíndromo:')
    palavra_invertida = palavra [:: -1]
    if palavra == palavra_invertida:
        print('a palavra',palavra,'é um políndormo')
    else:
        print('a palavra',palavra,'não é um políndormo') 

    

palindromo ()