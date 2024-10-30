def retornar_letras_unicas_string(mensagem):
    diferentesLetras = []
    quantidadeCadaLetra = []
    for letra in mensagem:
        if(letra not in diferentesLetras):
            diferentesLetras.append(letra)
            quantidadeCadaLetra.append(1)
        else:
            quantidadeCadaLetra[diferentesLetras.index(letra)]+=1
    
    return diferentesLetras, quantidadeCadaLetra
        



#TESTE DE CODIGO

palavra = input('Insira uma palavra: ')

diferentesLetras, quantidadeCadaLetra = retornar_letras_unicas_string(palavra)

print(f'Analisando a palavra "{palavra}", temos:')
for indice, letra in enumerate(diferentesLetras):
    print(f'{letra}, com {quantidadeCadaLetra[indice]} unidades')