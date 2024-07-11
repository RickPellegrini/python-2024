# %%

def valida_entrada():
     while True:
        try:
            numero = int(input('Escreva algum numero de 1 a 15:'))
            
        except ValueError:
            print('digital numero imbecil')
            continue

        if 1 <= numero <=15:
            return numero
        else:
            print('Entre com um numero valido.')


numero_sorte = 7

for i in range(3):

    numero = valida_entrada()
   
    if numero == numero_sorte:
        print('Voce acertou!')
        break


    elif numero > numero_sorte:
        print('Digite um numero mais baixo')
    else:
        print('Voce errou tente denovo')
# %%
