
x = 1

def escopo1():
    x = 2

    def escopo2():
        x = 3
        print(x)
    
    print(x)
    escopo2()


print(x)
escopo1()
escopo2()
escopo1()
print(x)