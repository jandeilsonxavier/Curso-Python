nome = 'jose jandeilson'
tamanho_nome = len(nome)
contador = 0
nova_string = '*'
print(tamanho_nome)

while contador < tamanho_nome:

    nova_string = nova_string + nome[contador] + '*'
       
    contador += 1

print(nova_string)