# %%

def operacao(op, *num):

    total = 0
    if op == 'soma':
        for i in num:
            total += i
    elif op == 'mult':
        total = 1
        for i in num:
            total *= i


    return total


operacao('mult',1,2,3,4,5,6,7,8)


# %%

dados = ['rick', 'calvo', 31, ['nah', 'elaine', 'josefina']]

nome, sobrenome, *_, ex = dados

print(nome)
print(sobrenome)
print(ex)

# %%




