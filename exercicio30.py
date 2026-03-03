pessoa = {
    'walace': 23,
    'gustavo':45,
}
print('dicionario normal:')
for nome , idade  in pessoa.items():
    print(f'{nome}: {idade}')


pessoa.update({'joao': 13})

def linha (x):
    print('_' * x)

linha(30)



print('dicionario atualizado:')
for nome , idade  in pessoa.items():
    print(f'{nome}: {idade}')


