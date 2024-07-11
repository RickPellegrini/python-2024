tipo_do_sorvete = input('Escolha o tipo do sorvete que gostaria: casquinha, cascao, cascudo\n')
sabor = input ('Escolha o tipo do sabor que gostaria: morango, creme, chocolate\n')
cobertura = input ('Escolha o tipo de cobertura que gostaria: caramelo, morango, chocolate ou sem cobertura\n')

valor = 0



# tipo do sorvete
if tipo_do_sorvete == ('casquinha'):
    valor += 1.50
    print('casquinha')

elif tipo_do_sorvete == ('cascao'):
    valor += 2.50
    print('cascao')

elif tipo_do_sorvete == ('cascudo'):
    valor += 3.50
    print('cascudo')

else:
    print('seu sorvete vai vir cagado')




# tipo da cobertura
if cobertura == ('caramelo'):
    valor += 1.50
    print('casquinha')

elif cobertura == ('morango'):
    valor += 2.50
    print('cascao')

elif cobertura == ('chocolate'):
    valor += 3.50
    print('cascudo')

elif cobertura == (''):
    pass

else:
    print('seu sorvete vai vir cagado')


print ('O sorvete do tipo',tipo_do_sorvete,'sabor',sabor, 'com cobertua de', cobertura,'fica no total de: ', valor )

# %%

nome = 'rick calvo'

print ("rick" in nome)