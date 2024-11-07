from dateutil.relativedelta import relativedelta #pip install python-dateutil
import datetime
#definindo variaveis que recebem as datas de nascimento
dataNascimento1 = input('Insira a primeira data de nascimento (no formato ano-mes-dia): ').strip()
dataNascimento2 = input('Insira a segunda data de nascimento (no formato ano-mes-dia): ').strip()

def calcular_diferenca_idade(dataNascimento1, dataNascimento2):
    #convertendo a data str para data
    data1_sprttime = datetime.datetime.strptime(dataNascimento1, '%Y-%m-%d')
    data2_sprttime = datetime.datetime.strptime(dataNascimento2, '%Y-%m-%d')
    
    #corrigindo a ordem, caso estejam erradas
    
    if(data1_sprttime < data2_sprttime):
        data1_sprttime, data2_sprttime = data2_sprttime, data1_sprttime
    #Pegando a diferenca atraves da biblioteca dateutil
    
    diferenca = relativedelta(data1_sprttime, data2_sprttime)
    
    return diferenca.years, diferenca.months, diferenca.days

diferencaAnos, diferencaMeses, diferencaDias = calcular_diferenca_idade(dataNascimento1, dataNascimento2)

print(f'\nDe acordo com as 2 datas fornecidas, a diferenca entre elas é de: {diferencaAnos} anos, {diferencaMeses} meses e {diferencaDias} dias.')