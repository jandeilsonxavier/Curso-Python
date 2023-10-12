frase = 'programaçao'.lower()
caracter_atual=''
i = 0
contador_repeticoes = 0


while i < len(frase):
    caracter_atual = frase[i]
    contador_repeticoes = frase.count(caracter_atual)
    print(f'{caracter_atual} = {contador_repeticoes}')
    i+=1 

    
