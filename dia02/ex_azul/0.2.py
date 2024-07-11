# %%
escolha = input('Maquina de agua, voce deseja agua com ou sem gas?\n')

quantidade = int(input("quantas aguas voce quer"))

total = 0 



if escolha == 'com':
    total = 1.50 * quantidade
    
elif escolha == 'sem':
    total = 2.50 * quantidade
else:
    print("faca uma escolha valida")

print('voce me deve', total)