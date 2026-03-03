frase_palavra = input ('digite uma palavra ou frase:')

vogais ='aeiouáéíóúâêôAEIOU'

total = 0

for vogal in vogais:
    total += frase_palavra.count (vogal)

print (total)