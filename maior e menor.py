num1 = input(print('digite o primeiro número: ')) 
num2 = input(print('digite o segundo número: ')) 
num3 = input(print('digite o terceiro número: ')) 
num4 = input(print('digite o quarto número: ')) 

numeros = [num1, num2, num3, num4]

maior= max(numeros)
menor= min(numeros)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")