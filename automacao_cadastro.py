filametos = {
        'cores': ['Branco', 'Preto', 'Cinza', 'Amarelo', 'Azul', 'Vermelho'],
        'pesos': ['1Kg', '250g'],
    }
nova_str = ''
for cor in filametos['cores']:
    for peso in filametos['pesos']:
        nova_str = (f'Descrição\
        O Filamento PLA Creality Ender uma excelente escolha para entusiastas da impressão 3D que buscam melhor qualidade de impressão e facilidade de uso. O Filamento PLA Creality não emite odores fortes durante a impressão, não é tóxico, e não necessita de impressora fechada, tornando-o ideal para uso doméstico, escolar e industrial.\
        O Filamento PLA é o filamento de maior facilidade de utilização, além de ser compatível com praticamente quase todas as impressoras 3D. O material PLA tem origem natural (amido de milho e cana-de-açúcar), o que o caracteriza como biodegradável.\
        Especificações\
        – Marca: Creality\
        – Material: PLA (ácido poliláctico)\
        – Diâmetro: 1.75mm\
        – Cor:', cor, '\
        – Peso:', peso,  '\
        – Temperatura de impressão: 190-220°C\
        – Temperatura da mesa: 50-60°C\
        – Tolerância de diâmetro: +/- 0.02 mm\
        – Resistência à tração: 60 MPa\
        – Alongamento na ruptura: 3%\
        – Densidade: 1.24 g/cm³\
        – Ponto de fusão: 150-160°C\
        Acompanha\
        01 – Filamento PLA Creality Ender 1.75mm 1kg - Cinza')
        print(nova_str)           