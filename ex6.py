#Peça ao usuário para digitar 3 números, em seguida mostre a ele esses números em ordem decrescente
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
numeros = [num1, num2, num3] 
numeros.sort(reverse=True)  
print('Os números em ordem decrescente são: ',numeros)
