#Peça ao usuário para digitar uma palavra e mostre quantas vogais ela tem
#palavra = input("Digite uma palavra: ")
#vogais = ["a", "e", "i", "o", "u"]  
#contador = 0  

#for letra in palavra:
   # for vogal in vogais: 
       # if (letra == vogal): 
           # contador += 1

#print(f"A quantidade de vogais na palavra {palavra} é de: {contador}")

#print(f"A palavra '{palavra}' tem {contador_vogais} vogais.")

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados
#numero1 = int (input('Digite o primeiro número:'))
#numero2 = int (input('Digite o segundo numero:'))
#numero3 = int (input('Digite o terceiro número:'))
#numero4 = int (input('Digite o quarto número:'))
#numero5 = int (input('Digite o quinto número:'))
#numero6 = int (input('Digite o sexto número:'))

#listaDePares = []

#istaDeNumeros = [numero1, numero2, numero3, numero4, numero5, numero6]

#for numero in ListaDeNumeros:
 #   if numero % 2 == 0:
  #      listaDePares.append(numero)

#if len(listaDePares) != 0:
 #   print(f"Os números áres digitados foram: {listaDePares}")
#else:
 #   print("A lista não tem nenhum número par!")

#Peça ao usuário para digitar 4 notas e faça a média delas
#nota1 = float (input('Digite a primeira nota:'))
#nota2 = float (input("Digite a segunda nota:"))
#nota3 = float (input("Digite a terceir nota:"))
#nota4 = float (input("Digite a quarta nota:"))
#média = (nota1 + nota2 + nota3 + nota4) /4

#print(f"A média das notas é {média}")

#Peça ao usuário para digitar o número de uma tabuada e faça ela do 1 ao 10
numeroDaTabuada =int(input("Digite o número que quer saber a tabuada: "))

for numero in range(1, 11):
    print(f"{numeroDaTabuada} X {numero} = {numeroDaTabuada * numero}")
