# %%
numero_sorte = 7

for i in range(3):

    while True:
        try:
            numero = int(input('Escreva algum numero de 1 a 15:'))
            break
        except ValueError:
            print('digital numero imbecil')

    if numero == numero_sorte:
        print('Voce acertou!')
        break


    elif numero > numero_sorte:
        print('Digite um numero mais baixo')
    else:
        print('Voce errou tente denovo')