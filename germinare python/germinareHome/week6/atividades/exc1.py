#INVERTENDO A MENSAGEM
mensagemUsuario = input('Insira a sua mensagem: ')
mensagemUsuarioInvertida = mensagemUsuario[::-1]

print(f'\n MENSAGEM ORIGINAL: "{mensagemUsuario}"')
print(f'\n MENSAGEM INVERTIDA: "{mensagemUsuarioInvertida}"')

#CONTANDO AS VOGAIS

quantidadeVogais = mensagemUsuario.lower().count('a')
quantidadeVogais += mensagemUsuario.lower().count('e')
quantidadeVogais += mensagemUsuario.lower().count('i')
quantidadeVogais += mensagemUsuario.lower().count('o')
quantidadeVogais += mensagemUsuario.lower().count('u')

print(f'\nA mensagem tem {quantidadeVogais} vogais')