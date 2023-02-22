# Factorial con recursividad 

x = 7

def facrecu(x):
    if x == 1:
        return 1
    else:
        return x * facrecu(x - 1)

print(facrecu(x))
