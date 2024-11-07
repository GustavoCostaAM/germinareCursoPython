#FUNCIONARA SOMENTE SE USAR UM DEFAULTDICT(LIST)
def exibirDict(dicionario):
    for chave, valor in dicionario.items():
        saidaValor = ', '.join(str(indice) for indice in valor)
        
        print(f'{chave} | {saidaValor}')


#METODO DE TRATAMENTO DO DICIONARIO:
from collections import defaultdict

dicionario = defaultdict(list)

dicionario['nome'].append('Gustavo')
dicionario['idade'].append(15)
dicionario['irmaos'].append('Ismael')
dicionario['irmaos'].append('Eduardo')

exibirDict(dicionario)