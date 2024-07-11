alturas = []

for i in range(4):
    a = int(input(f'Entre com a altura em cm {i+1}:\n'))
    alturas.append(a)
    
soma = sum(alturas)
print(soma)

