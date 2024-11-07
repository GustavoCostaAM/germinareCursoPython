import math
def tempoDowload():
    tamanhoArquivoMB = int(input('insira o tamanho do arquivo em Megabytes: '))
    conexao = int(input('insira a velocidade da sua conexao: '))
    
    tamanhoArquivoMBits = tamanhoArquivoMB*8
    tempoDeDowload = round(tamanhoArquivoMBits/conexao, 2)
    
    dowloadRapido = not(bool(math.floor(tempoDeDowload/60)))
    
    print(f'o tempo estimado de dowload é de {tempoDeDowload}')
    print('dowload rapido?', dowloadRapido)
    
tempoDowload()