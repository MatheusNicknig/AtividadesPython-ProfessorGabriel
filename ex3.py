#Peça ao usuário para digitar uma letra e verifique se ela é uma vogal ou consoante
letra = char(input('Digite uma letra: '))
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('A letra é uma vogal')
else:
    print('A letra é uma consoante')
