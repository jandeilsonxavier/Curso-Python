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
pergunta1 = perguntas[0]
pergunta2 = perguntas[1]
pergunta3 = perguntas[2]

print(f'Pergunta:', pergunta1['Pergunta'], '🤔' '\n')

print('Alternativas:\n')
for i in pergunta1['Opções']:
    print(f'',i)

resposta = input( '\n' 'Escolha uma das alternativas:')
if resposta == pergunta1['Resposta']:
    print('\n Acertou! \U0001f44F \U0001f44F \U0001f44F \n')
print('\n Errou \U0001f44E \U0001f44F \U0001f44F \n')



