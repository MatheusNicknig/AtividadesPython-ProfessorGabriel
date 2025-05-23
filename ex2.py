#Peça ao usuário para digitar dois números e verifique qual número é maior ou se os dois são iguais
num1 = int (input('digite um número'))
num2 = int (input('digite outro número'))
if num1 > num2:
    print(f'O número {num1} é maior que {num2}')
elif num2 > num1:
    print (f'O número {num1} é maior que {num2}')
elif num1 == num2:
    print('Os números são iguais')
