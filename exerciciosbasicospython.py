# Exercicio 1
# numero = int(input('Informe um número inteiro qualquer: '))
# print(f'O antecessor do número {numero} é {numero - 1}, e o sucessor é {numero + 1}')

# Exercicio 2
# numero = int(input('Informe um número inteiro qualquer: '))
# print(f'Este número com duas casas decimais fica assim: {numero:.2f}')

# Exercicio 3
# frase = 'Exercícios de Java'
# print(frase.replace('Java', 'Python'))

# Exercicio 3
# def numero_par_ou_impar(numero):
#     if numero % 2 == 0:
#         return f'O número {numero} é par'
#     return f'O número {numero} é impar'

# Exercicio 4
# numero = int(input('Informe um número inteiro qualquer: '))
# print(numero_par_ou_impar(numero))

# def numero_par_ou_impar(numero):
#     return numero % 2 == 0


# numero = int(input('Informe um número inteiro qualquer: '))

# if numero_par_ou_impar(numero):
#     print(f'O número {numero} é par')
# else:
#     print(f'O número {numero} é impar')


# 1. Classificação de Idade
# Peça a idade do usuário e classifique-o de acordo com a tabela:
# Menor de 12 anos → Criança
# Entre 12 e 17 anos → Adolescente
# 18 anos ou mais → Adulto

idade = int(input('Informe a sua idade: '))
if idade < 12 and idade >= 1:
    print(f'Criança')
elif idade >= 12 and idade <= 17:
    print(f'Adolescente')
elif idade > 18 and idade <= 100:
    print(f'Adulto')
else:
    print(f'Idade inválida')


# 2. Maior de Dois Números
# Solicite dois números ao usuário e exiba o maior deles. Caso sejam iguais, informe isso.

numero = int(input('Informe um número: '))
numero2 = int(input('Informe um outro número: '))

if numero > numero2:
    print(f'{numero} é maior que {numero2}')
elif numero == numero2:
    print(f'{numero} é igual a {numero2}')
else:
    print(f'{numero} é menor que {numero2}')


# 3. Verificação de Vogal ou Consoante
# Peça ao usuário para digitar uma letra e informe se é uma vogal (a, e, i, o, u) ou consoante.

letra = input('Digite uma letra: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra digitada é uma vogal.')
else:
    print(f'A letra digitada é uma consoante.')


# 4. Comparação de Senhas
# Solicite ao usuário que defina uma senha e, em seguida, peça para confirmá-la. Caso as senhas sejam iguais, exiba “Acesso permitido”, senão, exiba “Senhas não coincidem”.

senha1 = input('Digite uma senha: ')

senhaConfirmada = input('Confirme a sua senha: ')

if(senha1 == senhaConfirmada):
    print('Acesso permitido!')
else:
    print('Acesso negado!')

# 5. Cálculo de Média e Aprovação
# Peça ao usuário para digitar três notas e calcule a média. Se a média for maior ou igual a 7, o aluno está aprovado, caso contrário, está reprovado.

nota1 = float(input('Digite a primera nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <= 10:
    print(f'O aluno está aprovado com média: {media}!')
elif media < 7 and media >= 0:
    print(f'O aluno está reprovado com média: {media}!')
else:
    print('Média inválida!')

# 6. Escreva um programa que leia 3 números inteiros e imprima na tela os valores em ordem decrescente

numero1 = int(input('Digite um primeiro numéro inteiro: '))
numero2 = int(input('Digite um segundo numéro inteiro: '))
numero3 = int(input('Digite um terceiro numéro inteiro: '))

listaDeNumeros = [numero1, numero2, numero3]

print(f'A lista dos números em ordem decrescente é: {sorted(listaDeNumeros,reverse=True)}')


# 7. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz
# 	12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média.
# 	Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# 	Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a
# 	fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
# 	tempo gasto, a distância percorrida e a quantidade de litros utilizada na viagem. Dica: trabalhe com valores reais.

tempoGasto = int(input('Digite o valor do tempo gasto em horas: '))
velocidadeMedia = int(input('Digite o valor da velocidade média em KM/H: '))

distancia = tempoGasto * velocidadeMedia

litrosUsados = distancia / 12

print(f'O valor da velocidade média é de: {velocidadeMedia}KM/H \nO valor do tempo gasto é de: {tempoGasto} Horas \nO valor da distância percorrida é de: {distancia}KM \nA quantidade de litros usados na viagem foi de: {litrosUsados}L')
