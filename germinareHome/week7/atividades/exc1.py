emailUsuario = input('digite o email do usuario: ')

def validarEmail(email):
    #definindo variaveis
    emailValido = False
    errors = []
    email = email.lower()
   
    #criando bloco de if, com as condições precisas para retornar true se o email for valido
    if(email.count('@') == 1 and email.count('.com.br') == 1 and email.find('.com.br') > email.find('@')):
        emailValido = True
   
    #encontrando todos do email, e adicionando eles na lista errors
    if(email.find('.com.br') < email.find('@')):
        errors.append('.com.br deve ser na frente de @')
       
    if(email.count('.com.br') < 1):
        errors.append('falta .com.br')
    elif(email.count('.com.br') > 1):
        errors.append('muitos .com.br')
       
       
    if(email.count('@') < 1):
        errors.append('falta @')
    elif(email.count('@') > 1):
        errors.append('Muitos @')
   
   
   #fazendo return dos valores obtidos
    return emailValido, errors


#aplicando os resultados da função em variaveis
email_valido, errors = validarEmail(emailUsuario)
email_valido = 'valido' if email_valido else 'invalido'

#saida de dados
print(f'\nResultado da analise: o email inserio é {email_valido}\n')

if(email_valido == 'invalido'):
    print('Erros encontrados: ')
    for erro in errors:
        print(f'>{erro}')