numeroInt = int(input('digite um numero inteiro: '))

baseConversao = input('\nescolha a base de conversao:\n1: Converter para binario \n2: Converter para OCTAL\n3: Converter para HexaDecimal\n Numero da opcao escolhida: ')

if(baseConversao == "1"):
    print(bin(numeroInt)[2:])
elif(baseConversao == "2"):
    print(oct(numeroInt)[2:])
elif(baseConversao == "3"):
    print(hex(numeroInt)[2:])
else:
    print('erro, reinicie o programa e tente novamente.')

