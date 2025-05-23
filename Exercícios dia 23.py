#Peça um número N ao usuário e mostre todos os números de 1 até N.
#numeroDigitado = int (input("Digite um número para mostrar todos os número de 1 até o número digitado: "))
#for numero in range (1, numeroDigitado + 1):
#    print (f'{numero}')

#Peça ao usuário uma palavra e mostre ela ao contrário.
#palavraDigitada = str (input("Digite uma palavra: "))
#print(f"Você digitou: {palavraDigitada}")
#PalavraInvertida = palavraDigitada[::-1]
#print(f"A palavra que você digitou invertida fica: {PalavraInvertida}")

#Peça um número ao usuário e diga se ele é múltiplo de 3.
#NumeroDigitado = int (input("Digite um número para saber se ele é múltiplo de 3: "))
#if NumeroDigitado % 3 == 0:
#    print(f"O número {NumeroDigitado} é um múltiplo de 3!")
#else:
#    print(f"o número {NumeroDigitado} não é um múltiplo de 3!")

#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética.
Nome1 = str (input("Digite o primeiro nome: "))
Nome2 = str (input("Digite o segundo nome: "))
Nome3 = str (input("Digite o terceiro nome: "))
ListaNomes = [Nome1, Nome2, Nome3]
ListaNomes.sort(reverse=True)
print (f"Os nome digitados em ordem alfabética fica: {ListaNomes}")
