# %% 

idade = int(input('Entre ocm sua idade'))
cnh = input("voce tem cnh>?")

if idade >= 18 and cnh == 'sim':
    print ('liberado')

else:
    print('preso')


condicao = idade >= 18 and cnh == 'sim'
print (condicao)
