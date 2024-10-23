quantidadePregosTelheiros = int(input('Insira a quantidade de pregos telheiros que foram vendidos: '))
quantidadePregosQuadrados = int(input('Insira a quantidade de pregos quadrados que foram vendidos: '))


#funcao para calcular o valor arrecadado
def calcular_valor_arrecadado(quantidadePregosTelheiros, quantidadePregosQuadrados):
    ganhosPregosTelheiros = quantidadePregosTelheiros*1.05
    ganhosPregosQuadrados = quantidadePregosQuadrados*0.51
   
    ganhoTotal = ganhosPregosTelheiros + ganhosPregosQuadrados
   
    return ganhosPregosTelheiros, ganhosPregosQuadrados, ganhoTotal

#funcao para calcular, em reais, a comissao que terá que pagar

def calcular_comissao(ganhoTotal):
    comissao = ganhoTotal*0.10
    return comissao
   
   
#fazendo as chamadas das funcoes

ganhosPregosTelheiros, ganhosPregosQuadrados, ganhoTotal = calcular_valor_arrecadado(quantidadePregosTelheiros, quantidadePregosQuadrados)
comissao = calcular_comissao(ganhoTotal)

print(f'Ganhos por pregos telheiros: R${ganhosPregosTelheiros:.2f}')
print(f'Ganhos por pregos quadrados: R${ganhosPregosQuadrados:.2f}')
print(f'Ganhos totais: R${ganhoTotal:.2f}')
print(f'\nComissão a pagar: R${comissao:.2f}')