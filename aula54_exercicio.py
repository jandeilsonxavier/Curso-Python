"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""--------------------------------------Exercicio 1--------------------------------------------

num = input('Digite um número inteiro: ')
try:
    num_int = int(num)
    if num_int%2 == 0:
        print(f'O número {num_int} é par!')
    else:
        print(f'O número {num_int} é impar! ')
except:
    print(f'O número {num} não é inteiro! ')


#--------------------------------------Exercicio 2--------------------------------------------
hora = input('Informe a hora em número inteiro: ')
try:
    hora = int(hora)
    if hora>=0 and hora<=5:
            print('Boa madrugada')
    elif hora>=6 and hora<=11:
            print('Bom dia')
    elif hora>=12 and hora<=17:
            print('Boa tarde')
    elif hora>=18 and hora<=23:
            print('Boa noite')
    else:
           print('Não conheço essa hora')
except:
       print('Você não digitou um número inteiro! ')
"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)
if nome:
    if tamanho_nome<=4:
        print('Seu nome é curto')
    elif tamanho_nome==5 or tamanho_nome==6:
        print('Seu nome é normal')
    elif tamanho_nome>6:
        print('Seu nome é muito grande')
else:
    print('Por favor, digite seu primeiro nome!')
