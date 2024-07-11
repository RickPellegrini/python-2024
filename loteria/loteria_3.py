import random

def check_input():
    try:
        return int(input('Escreva algum numero de 1 a 15:'))
            
    except ValueError:
            return 'digital numero imbecil'
            
def check_interval(numero):
     '''checa se o numero passado esta entre o intervalo de 1 e 15 considerando ambos
     numero: int'''
     return 1 <= numero <= 15

def valida_entrada():
     '''essa funcao valida a entrada do usuario para garantir que ele nao vai quebra'''
     while True:
          numero = check_input()

          if type(numero) != int:
               print(numero)
               continue
          
          if check_interval(numero):
               return numero


numero_sorte = random.randint(1,15)

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
