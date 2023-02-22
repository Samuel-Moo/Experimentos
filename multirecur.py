# vamo a experimentar con recursividad
x = 32
y = 423

def multirecu(x, y):
    if x == 0:
        return 0
    elif x > 0:
        return y + multirecu(x - 1, y)
    elif x == 1:
        return y

print(multirecu(x, y))
