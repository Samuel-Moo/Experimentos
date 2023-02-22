# funcion pa hacer una pirámide RECURSIVA
y = input("How many levels do you want? ")



def pyramid(h):
    if h == 1: 
        return ["*"]
    elif h == 0:
        return [""]
    return [" "+p+" " for p in pyramid(h-1)]+["*"*(2*h-1)]

if y.isnumeric() == True:
    y = int(y)
    print(*pyramid(y), sep="\n")
else: 
    print("Character(s) not accepted.")



        
