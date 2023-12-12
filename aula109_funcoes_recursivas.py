# def fatorial(n):
#     if n == 1:
#         return 1 
#     return n * fatorial(n-1)

# print(fatorial(5))

def contagem(n):
    if n == 1:
        return 1 
    return n + contagem(n-1)

print(contagem(6))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))