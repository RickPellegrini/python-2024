# %%

total = 0

entrada = 'x'
while True:

    entrada = input('Entre com o valor do saldo: ')
    if entrada == '':
        break
    total += float(entrada)

print(total)