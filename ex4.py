senha = str(input('Digite uma senha: '))
confirmação = str(input('Confirme a senha: '))
if confirmação == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')