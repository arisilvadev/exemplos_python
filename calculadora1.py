# criar uma calculadora
#passo 1: pedir ao usuário que insira um número
#passo 2: pedir ao usuário que insira outro número
#passo 3: pedir ao usuário que defina qual operação ele quer fazer
#passo 4: usar estrutura de repetição
#passo 5: usar estrutura condicional
import os #importa ações do sistema operacional, como limpar a tela
import time #importa ações de tempo, como esperar para executar a próxima ação

while True:#enquanto VERDADEIRO, faça: loop infinito.
    
    calculadora = 'Calculadora 1.0'#nome do programa
    print(f'{calculadora:=^40}')#adiciona o item== e deixa o texto centralizado com ^
    num1 = float(input('Digite um número ou "0" para fechar o programa: '))
    num2 = float(input('Digite outro número ou "0" para fechar o programa: '))
    fim = ('Calculadora finalizada!')
  
    if num1 == 0 or num2 == 0:
        print(f'{fim:=^40}')
        break#determina o fim do programa de acordo com a ação do usuário
   
    operacao = input('Digite qual operação você quer fazer [+, -, *, /]: ')
    operadores_permitidos = '+-*/'
    if operacao not in operadores_permitidos:#not in: se não estiverem os caracteres estipulados antes
        print('Operador inválido!')
        time.sleep(2)#o programa vai aguardar 2 segundos para executar a próxima ação
        os.system('cls')#o comando "cls" limpa a tela antes da próxima iteração
        continue#determina que o código volte ao começo da repetição WHILE

    if len(operacao) > 1:#len: lê se foi digitado mais de um valor na variável
        print('Digite apenas um operador!')
        time.sleep(2)
        os.system('cls')
        continue
    if operacao == '+':
        # print(num1 + num2)
        print(f'O resultado da operação {num1} + {num2} é: {num1 + num2:.1f}')
        input('Aperte enter para continuar')#determina ação do usuário antes de limpar a tela
        # time.sleep(2)
        os.system('cls')
       
    elif operacao == '-':
        # print(num1 - num2)
        print(f'O resultado da operação {num1} - {num2} é: {num1 - num2:.1f}')
        input('Aperte enter para continuar')
        # time.sleep(2)
        os.system('cls')
        
    elif operacao == '*':
        # print(num1 * num2)
        print(f'O resultado da operação {num1} * {num2} é: {num1 * num2:.1f}')
        input('Aperte enter para continuar')
        # time.sleep(2)
        os.system('cls')
        
    else:
        # print(num1 / num2)
        print(f'O resultado da operação {num1} / {num2} é: {num1 / num2:.1f}')
        input('Aperte enter para continuar')
        # time.sleep(2)
        os.system('cls')



        
        