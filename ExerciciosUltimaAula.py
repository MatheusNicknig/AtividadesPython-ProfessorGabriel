#exercicio 1
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_no_intervalo(a, b):
    return [num for num in range(a, b + 1) if eh_primo(num)]

#Imprimindo um teste do exercicio na tela
print(eh_primo(7))
print(eh_primo(9))
print(primos_no_intervalo(1, 20))

#exercicio 2
def ordenar_sem_repeticao(lista):
    return sorted(set(lista))

#Imprimindo um teste do exercicio na tela
print(ordenar_sem_repeticao([5, 3, 5, 2, 2, 9]))

#Exercicio 3
def soma_digitos(n):
    return sum(int(digito) for digito in str(abs(n)))

#Imprimindo um teste do exercicio na tela
print(soma_digitos(12345))

#Exercicio 4
def eh_palindromo(texto):
    limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return limpo == limpo[::-1]

#Imprimindo um teste do exercicio na tela
print(eh_palindromo("arara"))
print(eh_palindromo("Python"))

#Exercicio 5
from collections import Counter

def frequencia_palavras(texto):
    palavras = texto.lower().split()
    return dict(Counter(palavras))

#Imprimindo um teste do exercicio na tela
print(frequencia_palavras("O gato pulou o muro e o cachorro viu o gato"))

#Exercicio 6
def media_lista(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)

#Imprimindo um teste do exercicio na tela
print(media_lista([10, 20, 30]))
print(media_lista([]))