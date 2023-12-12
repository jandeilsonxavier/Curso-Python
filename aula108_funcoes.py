
'''x = 1

def escopo1():
    global x
    x = 2

    def escopo2():
        global x
        x = 3
        print(x)

    print(x)    
    escopo2()

print(x)
escopo1()
print(x)

# def soma(x, y):
#     if x > 10:
#         return [10, 20]
#     return x + y
# soma1 = soma(2, 2)
# soma2 = soma(3, 3)
# print(soma1)
# print(soma2)
# print(soma(11, 55))'''
# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# print(soma(1, 2, 3))

def fatorial(n):
    if n == 1:
        return 1 
    return n * fatorial(n-1)

print(fatorial(5))

def contagem(n):
    if n == 1:
        return 1 
    return n * contagem(n-1)

print(contagem(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Exemplo de uso
resultado = fibonacci(9)
print(resultado)