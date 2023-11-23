perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
contador = 0
for x in range(3):
    print(f'Pergunta:', perguntas[x]['Pergunta'], '🤔' '\n')

    print('Alternativas:\n')
    for i, opcoes in enumerate(perguntas[x]['Opções']):
        print(f'{i}) {opcoes}')

    resposta = input( '\n' 'Escolha uma das alternativas:')
    if resposta == perguntas[x]['Resposta']:
        contador+=1
        print('\n Acertou! \U0001f44F \U0001f44F \U0001f44F \n')
    else:
        print('\n Errou! \U0001f44E \U0001f62D \n')
print('Você acertou', contador, 'de 3.')


