# %% ATIVIDADE PRÁTICA 01: 
#Crie uma função que receba um nome e imprima uma saudação personalizada.
# def saudacao(nome):
#     print(f"Olá, {nome}! Seja bem-vindo(a).")
    
# saudacao('Ari')
#-----------------------------------------------------------
# %% ATIVIDADE PRÁTICA 02:
# Crie uma função que receba um horário e imprima
# "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.

# import os

# def saudacao_por_horario():#função construída para receber horário e saudar o usuário de acordo com a hora inserida
#     while True:
#         try:
#             hora = int(input("Digite a hora atual (0 a 23): "))
#             if 0 <= hora < 12:
#                 print("Bom dia!")
#                 break
#             elif 12 <= hora < 18:
#                 print("Boa tarde!")
#                 break
#             elif 18 <= hora <= 23:
#                 print("Boa noite!")
#                 break#para de repetir o laço quando a condição for verdadeira(apenas números inteiros)
#             else:
#                 print("Horário inválido. Digite um número entre 0 e 23.")#garante apenas números positivos
#                                                                         #no intervalo 0 / 23
#         except ValueError:
#             print("Entrada inválida. Digite um número inteiro.")#garante apenas números inteiros

# while True:
    
#     saudacao = input('Digite [s] para ser saudado ou [f] para finalizar o programa: ').lower()
#     if saudacao == 'f':
#         print('Finalizando o programa!')
#         break
#     elif saudacao == 's':
#         saudacao_por_horario()
#         input('Digite enter para continuar: ')#condição para autorizar a limpeza da tela à cada iteração
#         os.system('cls')#efetua a limpeza da tela à cada iteração
#     else:
#         print('Opção inválida. Digite apenas [s] ou [f].')
    
    #SEGUNDO EXEMPLO:
    
# def saudacao_por_horario():
#     while True:
#         try:
#             hora = int(input("Digite a hora atual (0 a 23): "))
#             if 0 <= hora <= 23:#garante que os valores estão nesse intervalo
#                 if hora < 12:
#                     print("Bom dia!")
#                 elif hora < 18:
#                     print("Boa tarde!")
#                 else:
#                     print("Boa noite!")
#                 break  # sai do loop após entrada válida
#             else:
#                 print("Digite um número entre 0 e 23.")
#         except ValueError:
#             print("Entrada inválida. Digite um número inteiro.")
#------------------------------------------------------------------------

# %% ATIVIDADE PRÁTICA 03:
#Crie uma função que receba dois números e retorne a soma deles.

# def soma(a,b):
#     return a + b


# num1 = float(input('Digite o primeiro número para somar: '))
# num2 = float(input('Digite o segundo número para somar: '))

# resultado = soma(num1, num2)

# print(f'A soma do número {num1} e o número {num2} é: {resultado:.2f}')
#----------------------------------------------------------------------
# %% ATIVIDADE PRÁTICA 04:
# Crie uma função que receba dois números e retorne a
# subtração do primeiro pelo segundo.

# def subtrair(a,b):
#     return a - b


# num1 = float(input('Digite o primeiro número para subtrair: '))
# num2 = float(input('Digite o segundo número para subtrair: '))

# resultado = subtrair(num1, num2)

# print(f'O resultado da subtração do número {num1} pelo número {num2} é: {resultado:.2f}')
#----------------------------------------------------------------------------
# %% DESAFIO PRÁTICO:
# Crie uma calculadora com opções de soma, multiplicação,
# subtração, divisão e sair.

# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)

# Utilize funções de rotina para cada operação e funções de unidade lógica para
# realizar os cálculos.

def soma(a,b):
    return a+b 

def subtração(a,b):
    return a-b 

def multiplicação(a,b):
    return a*b

def divisão(a,b):
    if b == 0:
        return 'Erro! Divisão não pode ser por 0!'
    return a/b
    
def menu():
    print('\n==Calculadora 2.0==')
    print('[1] Soma.')
    print('[2] Subtração.')
    print('[3] Multiplicação.')
    print('[4] Divisão.')
    print('[5] Sair.')
    
while True:
    menu()
    opcao = input('Escolha uma operação: ')
    
    if opcao == '5':
        print('👋 Fechando calculadora!👋 ')
        break
    elif opcao in ['1','2','3','4']:
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
        except ValueError:
            print(' ❌ Erro! Digite apenas números! ❌ ')
            continue
        if opcao == '1':
            print(f'Resultado = ✔️​  {soma(num1, num2)}')
        elif opcao == '2':
            print(f'Resultado = ✔️​  {subtração(num1, num2)}')
        elif opcao == '3':
            print(f'Resultado = ✔️​  {multiplicação(num1, num2)}')
        elif opcao == '4':
            print(f'Resultado = ✔️​  {divisão(num1, num2)}')
    else:
        print(' ❌ Erro! Digite um número entre 1 e 5! ❌')