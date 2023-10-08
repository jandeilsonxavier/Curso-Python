#Calculadora com while
while True:
    primeiro_digito = input('Digite o primeiro número ')
    segundo_digito = input('Digite o segundo número ')
    operador = input("Digite um operador: '+' '-' '*' '/' : ")

    '''if primeiro_digito.isdigit() and segundo_digito.isdigit():
        print('digitos ok')
    else:
        print('Um ou ambos os números não são digitos, tente novemante')
        continue'''
    num_1 = 0
    num_2 = 0
    try:
        num_1 = float(primeiro_digito)
        num_2 = float(segundo_digito)
    except:
        print('Um ou ambos os números não são digitos, tente novemante')
        continue
    if operador in '+-*/':
        if operador == '+':
            print(f'{num_1} + {num_2} = {num_1+num_2:.2f}')
        elif operador == '-':
            print(f'{num_1} - {num_2} = {num_1-num_2:.2f}')
        elif operador == '/':
            print(f'{num_1} / {num_2} = {num_1/num_2:.2f}')
        elif operador == '*':
            print(f'{num_1} * {num_2} = {num_1*num_2:.2f}')
    else:
        print('O operador não é valido, tente novemante')
        continue

    sair = input("Digite 'S' para sair ").lower().startswith('s')
    if sair is True:
        break