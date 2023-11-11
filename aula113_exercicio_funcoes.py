def par_impar(numero):
    
    if numero%2 == 0:
            return 'par'
    return 'impar', numero

    '''return 'par' if numero%2 == 0 else 'impar'''
print(f'{numero} {par_impar(1)}')
print(par_impar(2))