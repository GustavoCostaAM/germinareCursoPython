from validate_docbr import CPF
from datetime import date
import random

cpf = CPF()
cpfGerado = cpf.generate(True)

data = date.today()

id = int(round(random.random(), 7)*(10**7))

nomeRemetente = input('Digite o nome da pessoa que esta realizando a transferencia: ')
agenciaRemetente = input('Digite o numero da agencia (4 digitos): ')
contaCorrenteRemetente = int(input('digite a conta corrente de quem esta realizando a transferencia: '))

nomeDestinatario = input('digite o nome do destinatario: ')
valorTransferencia = float(input('digite o valor a ser enviado: '))

if (len(agenciaRemetente) != 4):
    print('\n \033[31m ERRO: dados da agencia inseridos de forma incorreta')
else:
    print('\n \033[32m DADOS DO CLIENTE\033[m')
    print('\033[1m nome:\033[m Claudio')
    print(f'\033[1m agencia:\033[m {agenciaRemetente}')
    print('\033[1m conta corrente:\033[m 1234567')
    
    print('\033[34m ------------------------------------- \033[m')
    print('\n \033[32m DADOS DA TRANSFERENCIA\033[m')
    
    print(f'\033[1m para:\033[m {nomeDestinatario}')
    print('\033[1m instituicao:\033[m Picpay')
    print('\033[1m chave:\033[m germinatech@gmail.com')
    print(f'\033[1m cpf:\033[m {cpfGerado}')
    
    if (valorTransferencia > 1500):
        print(f'\033[34m valor: R${valorTransferencia}')
        print('\033[34m ------------------------------------- \033[m')
        print('\n \033[32m ID/TRANSACAO\033[m')
        print(f'\033[1m ID: \033[m {id}')
        print(f'\033[1m DATA: \033[m {data}')
    else:
        print(f'\033[31m valor: R${valorTransferencia}')
        print('\033[34m ------------------------------------- \033[m')
        print('\n \033[32m ID/TRANSACAO\033[m')
        print(f'\033[1m ID: \033[m {id}')
        print(f'\033[1m DATA: \033[m {data}')