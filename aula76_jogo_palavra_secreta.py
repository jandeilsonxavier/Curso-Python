import os

palavra_secreta = 'amor'
acertos = ''
tentativas = 0
resultado = ''
while True:
    entrada = input('Digite uma letra: ').lower()
    if len(entrada) >= 2 or entrada.isdigit() or entrada.isspace():
        print('Digite apenas uma letra!')
        continue
    else:
        tentativas += 1
    if entrada in palavra_secreta:
        acertos += entrada
        os.system('cls')
        print('Parabens vc acertou!')
    else:
        print('Tente novamente!')
    resultado = ''
    for i in palavra_secreta:
        if i in acertos:
            resultado += i
        else:
            resultado += '*'
    if resultado == palavra_secreta:
        
        print('Parabens você ganhou!')
        os.system('cls')
        break

    print(resultado)
    print(f'{tentativas=}')
    continue       
