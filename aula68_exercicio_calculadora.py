#Calculadora com while
while True:
    primeiro_digito = input('Digite o primeiro número ')
    segundo_digito = input('Digite o segundo número ')
    operador = input("Digite um operador: '+' '-' '*' '/' : ")

    digitos_validos = None

    '''if primeiro_digito.isdigit() and segundo_digito.isdigit():
        print('digitos ok')
    else:
        print('Um ou ambos os números não são digitos, tente novemante')
        continue'''

    try:
        num_1 = float(primeiro_digito)
        num_2 = float(segundo_digito)
        digitos_validos = True
    except:
        print('Um ou ambos os números não são digitos, tente novemante')
        continue

    sair = input("Digite 'S' para sair ").lower().startswith('s')
    if sair is True:
        break