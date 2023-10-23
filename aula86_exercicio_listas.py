import os
import time
compras = []
entrada = ''
item_excluir = ''
while True:
    entrada = input('Selecione uma opção: [i]-inserir [a]-apagar [m]-mostrar: ').lower()
    os.system('cls')
    if entrada == 'i':
        compras.append(input('Digite o nome do item para adicionar na lista: ').lower())
        print('Item adicionado a lista.')
        time.sleep(2)
        os.system('cls')
        continue
    elif entrada == 'a':
        item_excluir = input('Digite o nome do item para apagar: ').lower()
        os.system('cls')
        for i in compras:
            if i == item_excluir:
                compras.pop(compras.index(i))
                print('Item apagado da lista!')
                time.sleep(2)
                os.system('cls')
                continue
    elif entrada == 'm':
        for i in compras:
            print(i)
        time.sleep(4)
        os.system('cls')
        continue    
    else:
        print('Digite um das três opções!')
        time.sleep(2)
        os.system('cls')
        continue
        