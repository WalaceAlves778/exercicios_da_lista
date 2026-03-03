def fatorial_recurcivo(numero) :
    if numero == 0 or  numero ==1 :
        return 1
    else:
        return numero * fatorial_recurcivo(numero -1)


if  __name__ == '__main__':
    n = int(input ('Digite um numero inteiro pesitivo \npara calcular seu fatorial: '))
    try:
        resultado = fatorial_recurcivo(n)
    except RecursionError:
        print('O numero ou é muito grande ou negativo!')
    print(f'O fatorial de {n} é = {resultado}')