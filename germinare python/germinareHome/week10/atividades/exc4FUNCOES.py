#definindo as funcoes
def incluirNovoTel(dicionario_agenda, nome, *telefone):
    if(nome not in dicionario_agenda):
        dicionario_agenda[nome] = list(telefone)
    else:
        return 'Nome repetido'


def incluirTelefone(dicionario_agenda, nome, *telefone):
    if(nome in dicionario_agenda):
        dicionario_agenda[nome].extend(telefone)
    else:
        incluirNovoTel(dicionario_agenda, nome, *telefone)


def excluirTelefone(dicionario_agenda, nome, telefone):
    if(nome in dicionario_agenda):
        listaTelefones = dicionario_agenda[nome]
        listaTelefones.remove(telefone)
        
        dicionario_agenda[nome] = listaTelefones
        
        if(dicionario_agenda[nome] == []):
            del dicionario_agenda[nome]
    else:
        return 'Nome nao encontrado'
    

def excluirNome(dicionario_agenda, nome):
    try:
        del dicionario_agenda[nome]
    except NameError:
        return 'Nome nao encontrado'
    

def pedirNome():
    while True:
            nome = input('Insira o nome: ')
            if(nome.isalpha()):
                break
            
            print('insira um nome, apenas com letras, sem simbolos ou numeros. \n')
    
    return nome

def pedirTelefone():
    while True:
            telefones = input('Insira pelo menos 1 numero para adicionar(com espaco entre cada numero de telefone numeros): ').strip().split()
            number = True
            for telefone in telefones:
                if(not telefone.isnumeric()):
                    number = False
            
            if(number):
                break
                
            print('Insira telefones com somente NUMEROS\n')
    
    return telefones

def pedirTelefone_SEM_SPLIT():
    while True:
            telefone = input('Insira apenas 1 numero para adicionar: ').strip()
            if(telefone.isnumeric):
                return telefone
                
            print('Insira telefones com somente NUMEROS\n')

def exibir_agenda(dicionario_agenda):
    print(f'{'NOMES:':<15}|{'NUMEROS:'}')
    print('-'*40)
    for chave, valor in dicionario_agenda.items():
        stringNumero = ', '.join(str(indice) for indice in valor)
        print(f'{chave:<15}|{stringNumero}')