#Crie um programa que simule o crescimento populacional ao longo dos anos. O usuário deve inserir a população inicial, a taxa de crescimento anual (em decimal) e o número de anos. O programa deve calcular e imprimir a população após o número de anos especificado.

populacaoInicial = int(input('digite a populaçao inicial: \n'))
taxaCrescimento = float(input('insira a taxa de crescimento anual (em decimal) \n'))
anos = int(input('insira a quantidade de anos: \n'))

def populacaoFinal(populacaoInicial, taxaCrescimento, anos):
    populacaoFinal = populacaoInicial*((taxaCrescimento+1)**anos)
    
    print(f'uma populacao de {populacaoInicial} pessoas, com taxa de crescimento de {taxaCrescimento}% ao ano, durante {anos} anos, no final a populacao vai ser de {round(populacaoFinal)} pessoas.')
    
populacaoFinal(populacaoInicial, taxaCrescimento, anos)