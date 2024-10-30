def filtrar_dicionario(dicionario, valor):
    chavesEncontradas = []
    
    for chave, valorAtual in dicionario.items():
        if(valor in valorAtual):
            chavesEncontradas.append(chave)
    
    return chavesEncontradas




#TESTANDO A FUNCAO

Clientes = {
    'Nome': 'Ana Maria Braga',
    'Endereco': 'Av. Maria Augusta, s/n',
    'OperadoraCelular': 'Vivo',
    # continue adicionando outras chaves e valores conforme necessário
}

chavesEncontradas = filtrar_dicionario(Clientes, 'Maria')

for chave in chavesEncontradas: print(chave)



