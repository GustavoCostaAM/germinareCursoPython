import datetime

anoAtual = datetime.datetime.now().year

dicionario_Trabalhador = {}

dicionario_Trabalhador['Nome'] =  input('Insira o nome: ')
dicionario_Trabalhador['anoNascimento'] =  int(input('Insira o ano de nascimento: '))
dicionario_Trabalhador['carteiraDeTrabalho'] =  int(input('Insira a carteira de trabalho(insira 0 se nao tiver): '))

if(dicionario_Trabalhador['carteiraDeTrabalho'] == 0):
    print(f'\n')
    print(f'nome: {dicionario_Trabalhador['Nome']}')
    print(f'Ano de nascimento: {dicionario_Trabalhador["anoNascimento"]}')
    print('Nao tem carteira de trabalho')
else:
    dicionario_Trabalhador['anoContratacao'] = int(input('Insira o ano de contratacao: '))
    dicionario_Trabalhador['salario'] = float(input('Insira o salario: '))
    dicionario_Trabalhador['aposentadoria'] = 50-(anoAtual - dicionario_Trabalhador['anoNascimento'])
    print(f'\n')
    for chave, valor in dicionario_Trabalhador.items():
        print(f'{chave} tem o valor {valor}')