frase = 'programaçao'.lower()
caracter_atual=''
i = 0
contador_repeticoe = 0


while i < len(frase):
    caracter_atual = frase[i]
    contador_repeticoe = frase.count(caracter_atual)
    print(f'{caracter_atual} = {contador_repeticoe}')
    i+=1 

    
