entrada = input('[E]entrar [S]sair: ')
senha_usuario = input('Digite sua senha: ')
senha_permitida = '123456'

if entrada == 'E'and senha_usuario == senha_permitida:
    print('Seja bem vindo!')
elif entrada == 'S':
    print('Até breve!')
elif entrada != 'E' and 'S':
    print('Escolha uma entre as duas opções "E" ou "S" ')
else:
    print('Senha errada!')