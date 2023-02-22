# funcion pa hacer una pirámide 
x = int(input("How many levels do you want? \n"))

char = "*"
space = " " * x
print(space + char)
for i in range(x -1):
    char += "**"
    x = x - 1
    space = " " * x
    
    print(space + char)

