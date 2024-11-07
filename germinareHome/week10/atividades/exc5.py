from collections import defaultdict

def inverter_chave_valor_dicionario(estoque):
    novo_dicionario = defaultdict(list)
    for chave, valor in estoque.items():
        novo_dicionario[valor].append(chave)
       
    return novo_dicionario


#TESTE DA FUNCAO

dicionario = {
    '0175': 'camiseta',
    '5847': 'calca',
    '0822': 'tenis',
    '5555': 'camiseta',
    '4213': 'meia',
    '1111': 'calca'
}


novo_dicionario = inverter_chave_valor_dicionario(dicionario)


print(novo_dicionario)