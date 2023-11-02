import re
import sys
entrada = input('Digite seu CPF: ')
#Retirando caracteres indesejaveis 
#cpf = '700.265.874-32'\
#    .replace('.','') \
#   .replace(' ','') \
#    .replace('-','')

#Outra forma de retirar caracteres indesejaveis
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)
#Verificar se os numeros são repetidos
if entrada == entrada[0]*len(entrada):
    print('Voce digitou numeros repetidos')
    sys.exit()
multiplicacao = 0
soma = 0

# Calculo digito 1 *************************
for i in range(10,1,-1):
    multiplicacao = i*int(cpf[10-i])
    soma += multiplicacao


condicao = (soma*10) % 11
digito_1 = 0 if condicao > 9 else condicao
print('Digito1: ', digito_1)

# Calculo digito 2 *************************
multiplicacao = 0
soma = 0

for i in range(11,1,-1):
    multiplicacao = i*int(cpf[11-i])
    soma += multiplicacao

condicao = (soma*10) % 11
digito_2 = 0 if condicao > 9 else condicao
print('Digito2: ',digito_2)
print('CPF valido!')