
palavra = input('entre com uma palavra')

qtde = 0

for i in palavra:
    if i == "a":
        qtde += 1

print('a possui', qtde," na palavra",palavra)


# %%

palavra = 'banana'
palavra.count ('a')