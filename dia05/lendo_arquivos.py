# %%

arquivo = open('arquivo.txt', 'a')
arquivo.write('1')
arquivo.close()
# %%
arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
# %%

with open('arquivo.txt','r') as file:
    conteudo = file.read()

print (conteudo)