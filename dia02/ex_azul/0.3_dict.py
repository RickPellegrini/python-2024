tipo_do_sorvete = input('Escolha o tipo do sorvete que gostaria: casquinha, cascao, cascudo\n').lower()
sabor = input ('Escolha o tipo do sabor que gostaria: morango, creme, chocolate\n').lower()
cobertura = input ('Escolha o tipo de cobertura que gostaria: caramelo, morango, chocolate ou sem cobertura\n').lower()

valor = 0

sorvetes = {
    'casquinha': 1.00,
    'cascao': 2.50,
    'cascudo': 4.00
}


if tipo_do_sorvete in sorvetes: 
    valor += sorvetes [tipo_do_sorvete]

else:
    print('o sorvete vai vir cagado')

coberturas = {'caramelo': 1.5,
              'morango': 1.5,
              'chocolate': 1.5,
              '': 0}

if cobertura in coberturas: 
    valor += coberturas [cobertura]

else:
    print('o sorvete vai vir cagado')



print ('O sorvete do tipo',tipo_do_sorvete,'sabor',sabor, 'com cobertua de', cobertura,'fica no total de: ', valor )

# %%

nome = 'rick calvo'

print ("rick" in nome)