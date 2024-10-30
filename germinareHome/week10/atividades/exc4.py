import exc4FUNCOES

#criando fluxo de codigo

#MENU
dicionario_agenda = dict()
while True:
    print('\nO que deseja fazer?')
    print('[1] -> incluir novo telefone e nome')
    print('[2] -> incluir novo telefone EM um nome')
    print('[3] -> excluir um ou mais telefones DE um nome')
    print('[4] -> excluir UM nome')
    print('[5] -> exibir agenda')
    print('[6] -> encerrar programa')
    
    while True:
        try:
            opcao = int(input('sua opcao: '))
            
            if(not 1<=opcao<=6):
                print('Insira um valor ent5re 1 e 6\n')
            else:
                break
        except ValueError:
            print('insira apenas o numero da opcao\n')
            
    print('-'*40)
    
    if(opcao == 1):
        while True:
            nome = exc4FUNCOES.pedirNome()
            telefones = exc4FUNCOES.pedirTelefone()
            
            erro = exc4FUNCOES.incluirNovoTel(dicionario_agenda, nome, *telefones)
            if(erro == None):
                break
            
            print(f'\033[31m{erro}\033[m\n')
    
        print('Valores adicionados com sucesso')
        print('-'*40)
        
    elif(opcao == 2):
        nome = exc4FUNCOES.pedirNome()
        telefones = exc4FUNCOES.pedirTelefone()
        
        exc4FUNCOES.incluirTelefone(dicionario_agenda, nome, *telefones)
        
        print('Valores adicionados com sucesso')
        print('-'*40)
    elif(opcao == 3):
        
        while True:
            nome = exc4FUNCOES.pedirNome()
            telefone = exc4FUNCOES.pedirTelefone_SEM_SPLIT()
            
            erro = exc4FUNCOES.excluirTelefone(dicionario_agenda, nome, telefone)
            
            if(erro == None):
                break
            
            print(f'\033[31m{erro}\033[m\n')
        
        print('Valor excluido com sucesso')
        print('-'*40)
    elif(opcao == 4):
        while True:
            nome = exc4FUNCOES.pedirNome()
            erro = exc4FUNCOES.excluirNome(dicionario_agenda, nome)
            
            if(erro == None):
                break
            
            print(f'\033[31m{erro}\033[m\n')
            
        print('Valor excluido com sucesso')
        print('-'*40)
        
        
    elif(opcao == 5):
        exc4FUNCOES.exibir_agenda(dicionario_agenda)
    else:
        break
        
        
    