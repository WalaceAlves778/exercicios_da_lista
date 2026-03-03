
with open ('arquivo.txt') as  file:
    linhas =  sum(1 for line in file)
print(f'total de linhas :{linhas}')

