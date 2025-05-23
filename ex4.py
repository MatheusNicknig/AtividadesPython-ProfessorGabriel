#Peça ao usuário para digitar uma sena e para confirma-lá, se a senha for igual a confirmação acesso permitido, se não acesso negado
senha = str(input('Digite uma senha: '))
confirmação = str(input('Confirme a senha: '))
if confirmação == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')
