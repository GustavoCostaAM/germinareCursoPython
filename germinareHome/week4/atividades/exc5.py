print('\033[32m**************************Parte 1**************************')
print('\033[34;4mNessa parte iremos pedir as informaçoes gerais da corrida\033[m \n')

#informacoes gerais da corrida (print)
quantidadeCompetidores = int(input('Qual a quantidade de competidores da corrida?: '))
distancia = float(input('insira a distancia em kilometros, da corrida: '))
tipoCorrida = input('\nInsira o tipo de corrida \033[1mda mesma forma escrita abaixo:\n\033[4m TRILHA \n ASFALTO \n HIBRIDA\033[m \nSua resposta: ')
while(tipoCorrida != "TRILHA" and tipoCorrida != "ASFALTO" and tipoCorrida != "HIBRIDA"):
    print(f'nao foi possivel encontrar a opcao {tipoCorrida}, tente selecionando de acordo com as devidas instrucoes')
    tipoCorrida = input('nova resposta: ')
partesInput = 1
    
#colocando os competidores em uma lista
listaCompetidores = []
for quantidade in range(0, quantidadeCompetidores):
    listaCompetidores.append(quantidade)

#criando uma funcao para reutilizar o codigo de calcular os pontos de acordo com a quantidade de competidores inserida

def calculandoPontuacao(competidor):
    #criando variaveis
    nomeCompetidor = input(f'Insira o nome do competidor {competidor + 1}: ')
    tempoConclusao = int(input(f'\nPara o competidor {competidor + 1}, insira o tempo de conclusao em minutos: '))
    idade = int(input(f'\npara o competidor {competidor + 1}, insira a idade: '))
    genero = input(f'\npara o competidor {competidor + 1}, insira \033[1mMASCULINO, ou insira FEMININO\n\033[4mSua resposta:\033[m ')
    
    quebraRecordes = int(input('\nEle quebrou algum recorde? \nDigite 1 se a resposta for sim, e 2 se a resposta for nao \n \033[4msua resposta:\033[m '))
    infracoesCorteCaminho = int(input('\nselecione a quantidade de infracoes cometidas por cortes de caminho: '))
    infracoesAjudaExterna = int(input('Insira a quantidade de infracoes cometidas por receber ajudas externas: '))
    print('\n')
    
    #calculando os pontos
    
    pontos = 0
    
    #pontos pelo tempo de conclusao:
    if(tempoConclusao < 30):
        pontos = pontos + 100
    elif(tempoConclusao >= 30 and tempoConclusao <= 60):
        pontos = pontos + 70
    else:
        pontos = pontos + 40
    
    #pontos pela idade:
    
    if(idade < 18):
        pontos = pontos + 20
    elif(idade >= 18 and idade <= 30):
        pontos = pontos + 10
    elif(idade >= 46 and idade <= 60):
        pontos = pontos + 20
    else:
        pontos = pontos + 25
    
    #pontos pelo genero:
    
    if(genero == "FEMININO"):
        pontos = pontos + 5
        
    #pontos por quebra de recordes:
    
    if(quebraRecordes == "1"):
        pontos = pontos + 50
    
    #pontos por infraçoes:
    
    if(infracoesCorteCaminho > 0):
        pontos = pontos - 10*int(infracoesCorteCaminho)
    elif(infracoesAjudaExterna):
        usuarioDesclassificado = True
    
    #pontos pelo tipo de corrida
    
    if(tipoCorrida == "TRILHA"):
        pontos = pontos + ((pontos/100)*10)
    elif(tipoCorrida == "HIBRIDA"):
        pontos = round(pontos + (pontos/100*5)*distancia)
        
    return pontos, nomeCompetidor, tempoConclusao, idade, genero, quebraRecordes, infracoesCorteCaminho, infracoesAjudaExterna
    
#array em que vai armazenar todos os pontos de cada competidor individualmente
#lembrar que a posicao de cada array equivale a mesma posicao do nome e do numero dos competidores dentro do array
listaTodosPontos = []
listaTodosNomes = []
listaTodosTempoConclusao = []
listaTodasIdades = []
listaTodosGeneros = []
listaQuebraRecordes = []
listaCortesCaminho = []
listaAjudasExternas = []
listaCompetidoresDesclassificados = []

#armazenando os devidos dados no array, e calculando os pontos atraves da funcao, logo depois fazendo um print organizado das informacoes atraves de uma estrutura de repeticao for

for numero, competidor in enumerate(listaCompetidores):
    print(f'\033[32m************************** {f'parte {partesInput + 1}'} **************************')
    print(f'\033[34;4mNessa parte iremos pedir as informaçoes a respeito do competidor {numero + 1}\033[m \n')
    partesInput = partesInput + 1
    
    pontos, nomes, tempoConclusao, todasIdades, generos, quebraRecordes, cortesCaminho, ajudasExternas = calculandoPontuacao(numero)
    
    listaTodosPontos.append(pontos)
    listaTodosNomes.append(nomes)
    listaTodosTempoConclusao.append(tempoConclusao)
    listaTodasIdades.append(todasIdades)
    listaTodosGeneros.append(generos)
    listaQuebraRecordes.append(quebraRecordes)
    listaCortesCaminho.append(cortesCaminho)
    listaAjudasExternas.append(ajudasExternas)

#RELATORIO:

print(f'\033[32m************************** RELATORIO FINAL**************************\033[m\n')

print(f'Nessa corrida, participaram \033[1m{quantidadeCompetidores}\033[m pessoas')
print(f'{listaTodosGeneros.count("FEMININO")} meninas')
print(f'{listaTodosGeneros.count("MASCULINO")} meninos\n')

print(f'Nessa corrida, participaram {len(set(listaTodasIdades))} idades diferentes\n')

print('\033[1mPODIO:\033[m\n')

print('\033[PRIMEIRO LUGAR:\033[m\n')

primeiroLugar = [max(listaTodosPontos), listaTodosPontos.index(max(listaTodosPontos))]

print(f'{listaTodosNomes[primeiroLugar[1]]}, com {primeiroLugar[0]} pontos.\n')

print('principais detalhes do participante:\n')

print(f'Tempo de corrida: {listaTodosTempoConclusao[primeiroLugar[1]]} minutos.')

print(f'idade: {listaTodasIdades[primeiroLugar[1]]} anos')

if(listaQuebraRecordes[primeiroLugar[1]] == "1"):
    print(f'O competidor quebrou recordes oficiais')
else:
    print(f'O competidor nao quebrou recordes oficiais')
    
print(f'O competidor fez, no total, {listaTodosPontos[primeiroLugar[1]]} pontos')






print('\033[SEGUNDO LUGAR:\033[m\n')

listaTodosPontos[primeiroLugar[1]] = -1
segundoLugar = [max(listaTodosPontos), listaTodosPontos.index(max(listaTodosPontos))]

print(f'{listaTodosNomes[segundoLugar[1]]}, com {segundoLugar[0]} pontos.\n')

print('principais detalhes do participante:\n')

print(f'Tempo de corrida: {listaTodosTempoConclusao[segundoLugar[1]]} minutos.')

print(f'idade: {listaTodasIdades[segundoLugar[1]]} anos')

if(listaQuebraRecordes[segundoLugar[1]] == "1"):
    print(f'O competidor quebrou recordes oficiais')
else:
    print(f'O competidor nao quebrou recordes oficiais')
    
print(f'O competidor fez, no total, {listaTodosPontos[segundoLugar[1]]} pontos')



listaTodosPontos[segundoLugar[1]] = -1
terceiroLugar = [max(listaTodosPontos), listaTodosPontos.index(max(listaTodosPontos))]


print('\033[TERCEIRO LUGAR:\033[m\n')

print(f'{listaTodosNomes[terceiroLugar[1]]}, com {terceiroLugar[0]} pontos.\n')

print('principais detalhes do participante:\n')

print(f'Tempo de corrida: {listaTodosTempoConclusao[terceiroLugar[1]]} minutos.')

print(f'idade: {listaTodasIdades[terceiroLugar[1]]} anos')

if(listaQuebraRecordes[terceiroLugar[1]] == "1"):
    print(f'O competidor quebrou recordes oficiais')
else:
    print(f'O competidor nao quebrou recordes oficiais')
    
print(f'O competidor fez, no total, {listaTodosPontos[terceiroLugar[1]]} pontos')