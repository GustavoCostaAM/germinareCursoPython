# Criando variaveis que recebem valores de entrada
valorEmprestimo = float(input('Qual valor do emprestimo voce deseja? '))
rendaMensal = float(input('Qual sua renda mensal? '))

scoreMaior = input('Seu score de créditos é acima de 450 pontos? \n digite: \n 1- Se a resposta for sim \n 2- Se a resposta for não \n sua resposta: ')
dividasAtivas = input('você não possui dividas ativas? \n Digite: \n 1- Para não \n 2- Para sim \n Sua resposta: ')
funcionarioPublico = input('Voce é um funcionario publico? \n Digite: \n 1- Para não \n 2- Para sim \n Sua resposta: ')
openBanking = input('Você concorda em compartilhar seus dados de outros bancos através do open banking? \n Digite: \n 1- Para não \n 2- Para sim \n Sua resposta: ')
rendaMensalDobroValor = False
# Definindo se o scoreMaior é maior que 450 ou menor, se a resposta do input for diferente de 1 e 2, vai retornar um erro

if(scoreMaior == "1"):
    scoreMaior = True
elif(scoreMaior == "2"):
    scoreMaior = False
elif(scoreMaior != "1" and scoreMaior != "2"):
    print(f'\033[31m Houve um problema, opção "{scoreMaior}" não existe. Favor desconsiderar as proximas operações e reiniciar o sistema.')
    scoreMaior = "ERRO"
    
# Definindo se o cliente possui dividas ativas, se a resposta do input for diferente de 1 e 2, vai retornar um erro

if(dividasAtivas == "2"):
    dividasAtivas = False
elif(dividasAtivas == "1"):
    dividasAtivas = True
elif(dividasAtivas != "1" and dividasAtivas != "2"):
    print(f'\033[31m Houve um problema, opção "{dividasAtivas}" não existe. Favor desconsiderar as proximas operações e reiniciar o sistema.')
    dividasAtivas = "ERRO"
    
# Definindo se o cliente é funcionario publico, se a resposta do input for diferente de 1 e 2, vai retornar um erro

if(funcionarioPublico == "1"):
    funcionarioPublico = False
elif(funcionarioPublico == "2"):
    funcionarioPublico = True
elif(funcionarioPublico != "1" and funcionarioPublico != "2"):
    funcionarioPublico = "ERRO"
    print(f'\033[31m Houve um problema, opção "{funcionarioPublico}" não existe. Favor desconsiderar as proximas operações e reiniciar o sistema.')

# Definindo open banking, se a resposta do input for diferente de 1 e 2, vai retornar um erro
    
if(openBanking == "1"):
    openBanking = False
elif(openBanking == "2"):
    openBanking = True
elif(openBanking != "1" and openBanking != "2"):
    openBanking = "erro"
    
# Definindo se a renda mensal é pelo menos o dobro do valor solicitado

if(rendaMensal >= rendaMensal * 2):
    rendaMensalDobroValor = True
else:
    rendaMensalDobroValor = False
    
# Contando a pontuação
pontuacao = 0

if(scoreMaior == True):
    pontuacao = pontuacao+ 1

if(dividasAtivas == False):
    pontuacao = pontuacao + 1
    
if(funcionarioPublico == True):
    pontuacao = pontuacao + 1
    
if(openBanking == True):
    pontuacao = pontuacao + 1

print(f'sua pontuacao foi de {pontuacao}')

if(pontuacao <= 2):
    valorAprovado = round((valorEmprestimo/100)*20)
    print(f'Aprovado com restrições, valor Aprovado: R${valorAprovado}')
elif(pontuacao == 3 or pontuacao == 4):
    valorAprovado = round((valorEmprestimo/100)*60)
    print(f'Aprovado com desconto, valor Aprovado: R${valorAprovado}')
elif(pontuacao == 5):
    valorAprovado = valorEmprestimo
    print(f'Aprovação total, valor aprovado: R${valorAprovado}')
elif(scoreMaior == "ERRO" or dividasAtivas == "ERRO" or funcionarioPublico == "ERRO"):
    print('Houve um erro no processamento de algum de seus dados, tente novamente.')