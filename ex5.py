#Peça ao usuário para digitar 3 notas, se a média do aluno for maior ou igual a 7 o aluno foi aprovado, se não reprovado
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) /3
if media >=7:
    print('Aprovado')
else:
    print('Reprovado')
