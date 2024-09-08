#Você precisar criar um gerador de senhas para o um sistema qualquer. O seu programa deverá pedir para o usuário criar uma senha e a senha deve seguir as seguintes regras: • Deve ter pelo menos 8 caracteres. • Deve conter pelo menos uma letra maiúscula e uma letra minúscula. • Deve conter pelo menos um caractere especial (considere apenas esses: ! @ # $ %). O programa deve validar se a senha atende a esses critérios e informar ao usuário se a senha é válida ou não

password = input('insira sua senha: ')
letras = list(password) #divide cada letra da senha em um array

#vendo quantos caracteres especiais tem:
especial = int(letras.count('!')) + int(letras.count('@')) + int(letras.count('#')) + int(letras.count('$')) + int(letras.count('%'))

if(len(password) >= 8 and any(letras.isupper() for letras in letras) and any(letras.islower() for letras in letras) and especial >= 1):
    print('A senha forncida cumpre com os resquisitos fornecidos')
else:
    print('a senha fornecida nao cumpre com os resquisitos')