#criando as listas de acordo com as informaçoes sobre os cadidatos

candidatosNome = []
candidatosNumeroCorrespondende = []

votosTotais = 0
votosInvalidos = 0

            #definindo as informaçoes da lista:

#definindo a lista dos nomes dos candidatos
contadorWhile = 1
print(f'Iremos pedir para que voce insira os nomes dos usuarios, digite "cancelar" quando querer parar de inserir usuarios.\n')
while True:
    nome = input(f'Para o candidato {contadorWhile}, insira seu nome: ')
    if(nome.lower() == 'cancelar'):
        print('\n')
        contadorWhile = 0
        break
    else:
        candidatosNome.append(nome)
    contadorWhile+=1
    
print(candidatosNome)

numerosDeCandidatos = len(candidatosNome)
#definindo o numero correspondente a cada candidato:
while(contadorWhile < len(candidatosNome)):
    candidatosNumeroCorrespondende.append(str(contadorWhile))
    contadorWhile +=1
print(candidatosNumeroCorrespondende)

            #realizando a votaçao
contadorWhile = 0

#organizando a lista de numeros de votos, o ultimo valor é correspondende a o voto em branco
numerosVotos = []
while contadorWhile <= len(candidatosNome):
    numerosVotos.append(0)
    contadorWhile +=1
    
#parte da votaçao
votantes = int(input('insira a quantidade de pessoas que irao votar: '))
contadorWhile = 0
contadorTexto = 0
while(contadorWhile < votantes):
    print(f'----------------------------')
    print(f'Voto {contadorWhile+1}')
    print(f'responda o numero de acordo com o numero do candidato: ')

    while(contadorTexto < numerosDeCandidatos):
        print(f'[{candidatosNumeroCorrespondende[contadorTexto]}] para {candidatosNome[contadorTexto]}')
        contadorTexto +=1
    print('[branco] para votar em branco')
    votoUsuario = input('Seu voto: ')
    
    
    
    if(votoUsuario not in candidatosNumeroCorrespondende and votoUsuario.strip().lower() != 'branco'):
        votosInvalidos += 1
        print('voto invalido, por isso, nao será computado.')
    elif(votoUsuario.strip().lower() == 'branco'):
        numerosVotos[-1] +=1
        print(f'voto registrado em branco\n')
    else:
        posicaoCandidato = candidatosNumeroCorrespondende.index(votoUsuario)
        numerosVotos[posicaoCandidato] +=1
        print(f'voto registrado para o candidato {candidatosNome[posicaoCandidato]}, com numero {votoUsuario}.')
              
    votosTotais +=1
    contadorWhile +=1
    contadorTexto = 0
    
    
#DEFININDO OS RESULTADOS DA VOTACAO
if(votosInvalidos == votosTotais):
    print('Todos os votos foram invalidos, impossivel realizar uma saida de dados com exito.')
else: 
    votosEmBranco = numerosVotos[-1]
    del(numerosVotos[-1])
    
    MaiorQuantidadeVotos = max(numerosVotos)
    if(numerosVotos.count(MaiorQuantidadeVotos) >=2):
        vencedor = 'empate'
    else:
        vencedor = numerosVotos.index(MaiorQuantidadeVotos)
        percentualDeVotos = MaiorQuantidadeVotos/(votosTotais-votosInvalidos)*100
            

                            #FAZENDO A SAIDA DE DADOS
                                        
    #definindo o total de votos
    contadorWhile = 0

    #definindo o numero total de votos validos (Sem contar os )

    print(f'----------------------------RESULTADOS----------------------------')
    print(f'No total, tiveram {votosTotais} votos totais')
    print(f'No total, {votosTotais - votosInvalidos} votos validos\n')
    if(vencedor == 'empate'):
        print('Ninguem venceu a votaçao devido a um empate, portanto, terá um segundo turno.')
    else:
        print(f'O vencedor foi {candidatosNome[vencedor]}, com {MaiorQuantidadeVotos} votos.')
        print(f'O vencedor ganhou com {percentualDeVotos:.2f}% dos votos validos')