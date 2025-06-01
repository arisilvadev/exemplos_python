# Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem 
# informando quantas tentativas restam. Se o usuário acertar, 
# uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.



# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem
# de "Acesso bloqueado" repetida três vezes.

usuario_correto = 'admin'
senha_correta = '123'

for i in range(3):
    usuario = input('Digite o login do usuário: ')
    senha = input('Digite a senha do usuário: ')
    if usuario == usuario_correto and senha == senha_correta:
        print('Seja bem vindo ao sistema!')
        break
    else:
        print(f'Tentativas restantes: {2 - i}')
print('Acesso bloqueado!')