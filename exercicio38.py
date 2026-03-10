with open ('arquivo.txt','a' ) as  file:
    add_linhas= input ('digite algo para adicionar ao texto:')
    file.write(f'\n{add_linhas}')
    file.close ()
    
with open('arquivo.txt','r',encoding= 'UTF-8') as f:
        linhas = f.readlines()
        for linha in linhas:
         print(linha)
