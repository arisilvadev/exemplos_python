# # escrever um código com tudo o que se aprendeu até aqui!
# #estruturas de decisão
# # Faça um Programa que peça dois números e imprima o maior deles.

# num_1 = input('Digite o número 1: ') #função "input" sempre retorna um objeto de valor str

# num_2 = input('Digite o número 2: ')

# try:
#     num_1 = int(num_1)

#     if num_1 > num_2:
#         print('O número 1 é maior que o número 2!')
#     else:
#         print('O número 2 é maior que o número 1!')
# except:
#     print('Digite um número inteiro')




#exercício 02 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# valor = float(input('Digite qualquer valor na tela: '))

# if valor > 0:
#     print(f'O valor {valor} é positivo!')
# elif valor < 0:
#     print(f'O valor {valor} é negativo!')

# print('Fim do programa.')

#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# nome = input('Digite seu nome: ')
# sexo = input('Digite "M" para masculino ou "F" para feminino: ')

# if sexo == 'M' or sexo == 'm':
#     print(f'{nome} é do sexo "masculino".')
# elif sexo == 'F' or sexo == 'f':
#     print(f'{nome} é do sexo "feminino".')
# else:
#     print('Sexo inválido!')

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
# produto_1 = float(input('Digite o valor do produto 1: '))
# produto_2 = float(input('Digite o valor do produto 2: '))
# produto_3 = float(input('Digite o valor do produto 3: '))

# if produto_1 < produto_2 and produto_1 < produto_3:
#     print('O produto 1 está mais barato. Você deve comprá-lo!')
# elif produto_2 < produto_1 and  produto_2 < produto_3:
#     print('O produto 2 está mais barato. Você deve comprá-lo!')
# else:
#    print('O produto 3 está mais barato. Você deve comprá-lo!')

# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# numero_1 = int(input('Digite o número 1: '))
# numero_2 = int(input('Digite o número 2: '))
# numero_3 = int(input('Digite o número 3: '))

# if numero_1 > numero_2 and numero_2 > numero_3:
#     print(f'{numero_1:-^10}\n{numero_2:-^10}\n{numero_3:-^10}')
# elif numero_1 > numero_3 and numero_3 > numero_2:
#     print(f'{numero_1:-^10}\n{numero_3:-^10}\n{numero_2:-^10}')
# elif numero_2 > numero_1 and numero_1 > numero_3:
#     print(f'{numero_2:-^10}\n{numero_1:-^10}\n{numero_3:-^10}')
# elif numero_2 > numero_3 and numero_3 > numero_1:
#     print(f'{numero_2:-^10}\n{numero_3:-^10}\n{numero_1:-^10}')
# if numero_3 > numero_1 and numero_1 > numero_2:
#     print(f'{numero_3:-^10}\n{numero_1:-^10}\n{numero_2:-^10}')
# elif numero_3 > numero_2 and numero_3 > numero_1:
#     print(f'{numero_3:-^10}\n{numero_2:-^10}\n{numero_1:-^10}')

# print('-'* 10, "Fim do programa", '-'* 10)
# print('#' * 40)

#  exercicio 0028: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante :  aumento de 5%
#     Após o aumento ser realizado, informe na tela:
# 
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.
   
# salario_anterior = float(input("Digite seu salário atual: "))
# salario_atual = 0.0
# diferenca_entre_salarios = 0.0
# percentual_de_aumento = 0.0

# if salario_anterior <= 280:
#     percentual_de_aumento = 20
# elif salario_anterior <= 750:
#     percentual_de_aumento = 15
# elif salario_anterior <= 1500:
#     percentual_de_aumento = 10
# else:
#     percentual_de_aumento = 5

# diferenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
# salario_atual = salario_anterior + diferenca_entre_salarios
# print(f"Seu salário antes do reajuste era de R$ {salario_anterior:.2f}")
# print(f"Seu salário foi aumentado em {percentual_de_aumento}%")
# print(f"Seu salário foi aumentado em R${diferenca_entre_salarios:.2f}")
# print(f"Seu salário atual é de R$ {salario_atual:.2f}")


# numero = 10
 
# if numero > 1:
#     if numero > 2:
#         if numero > 3:
#             print('Número maior que 3')
#         else:
#             print('Número menor que 3')
#     else:
#         print('Número menor que 2')
# else:
#     print('Número menor que 1')

# variavel = input('Digite o seu nome: ')
# nome_contrario = variavel[: : -1]
# print(nome_contrario)
# letra_final = variavel[-1]
# print(f'A letra final do seu nome é:' , letra_final)
# letra_inicial = variavel[0]
# print(f'A letra inicial do seu nome é: ', letra_inicial)
# print(f'Seu nome tem ' , len(variavel), 'carateres.')


# nome = str(input("Digite o nome do aluno: "))
# nota_1 = float(input("Digite a nota 1 do aluno " + nome + ": "))
# nota_2 = float(input("Digite a nota 2 do aluno " + nome + ": "))
# nota_3 = float(input("Digite a nota 3 do aluno " + nome + ": "))
# media = (nota_1 + nota_2 + nota_3) / 3
# fim = ('Fim do programa')


# if(media >=7):
#     linha_1 = f'Parabéns! Você foi "aprovado" e sua média é: {media:.2f}'
#     print(linha_1)
# elif(media >=5):
#     linha_2 = f'Você está de "recuperação" e sua média é: {media:.2f}'
#     print(linha_2)
#     print("Você precisa estudar mais!")
# elif(media <5):
#     linha_3 = f'Você está "reprovado" e sua média é: {media:.2f}'
#     print(linha_3)
#     print("Você terá uma outra oportunidade no ano seguinte")
# else:
#     print("Digite um valor válido")

# print(f'{fim:-^40}')
# print(40 * '-')
   

"""escrever um código que receba dois valores em números e retornar se um número
é maior que o outro ou menor que o outro"""

# numero_1 = (input("Digite o primeiro valor:"))
# numero_2 = (input("Digite o segundo valor:"))

# if (numero_1>numero_2):
#     print(f'o valor {numero_1= }  é maior que o valor {numero_2= }')
# else:
#     print(f'o valor {numero_1= } é menor que o valor {numero_2= }')


# print("Fim do programa")

# variavel = 'ABC'
# print(f'{variavel}')
# print(f'{variavel:<15}')
# print(f'{variavel:-^20}')
# print(60 * '-')
# print('Fim do programa')
   

# velocidade = int(input('Digite em que velocidade estava o veículo: ')) #lembrar:f2 renomeia a variável
# local_carro = int(input('Digite em que km da estrada estava o veículo: '))
# fim = ('Fim do programa!')
# #lembrar: se for usar uma CONSTANTE usar sempre letras maiúsculas!
# RADAR_1 = 61
# LOCAL_1 = 100
# RANGE = 1


# # if velocidade > RADAR_1:
# #     print('Você ultrapassou o limite de velocidade permitida!')

# if local_carro >= (LOCAL_1 - RANGE) and \
# local_carro <= (LOCAL_1 + RANGE) and \
# velocidade > 60:
#     print(f'-' * 10,'Você ultrapassou o limite de velocidade e foi multado!', '-' * 10)
# else:
#     print('Você passou dentro do limite de velocidade e não foi multado.')

# print(f'{fim:-^40}')
# print(id(velocidade))#comando "id" serve para mostrar a identidade da variável


# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
# exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

# hora = input('Digite a hora atual: ')
# fim = ('Fim do programa!')

# try:
#     hora = float(hora)

#     if hora == 0 and hora <=11:
#         print('Bom dia!')
#     elif hora > 11 and hora <= 17:
#         print('Boa tarde!')
#     else:
#         print('Boa noite!')

# except:
#     print('Digite uma hora válida!')
# print(f'{fim:-^40}')


# Faça um programa que peça o primeiro nome do usuário. 
# Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, 
# escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".


# nome = input('Digite o seu nome: ')
# fim = ('Fim do programa!')

# if len(nome) <4:
#     print(f'Seu nome é muito curto e tem {len(nome)} letras.')
#     print(f'Seu nome ao contrário é: {nome[::-1]}')
#     print(f'A última letra do seu nome é: {nome[-1]}')
#     print(f'A primeira letra do seu nome é: {nome[0]}')
# elif len(nome) >=5 and len(nome) <=6:
#     print(f'Seu nome é normal e tem {len(nome)} letras.')
#     print(f'Seu nome ao contrário é: {nome[::-1]}')
#     print(f'A última letra do seu nome é: {nome[-1]}')
#     print(f'A primeira letra do seu nome é: {nome[0]}')
# else:
#      print(f'Seu nome é muito grande e tem {len(nome)} letras.')
#      print(f'Seu nome ao contrário é: {nome[::-1]}')
#      print(f'A última letra do seu nome é: {nome[-1]}')
#      print(f'A primeira letra do seu nome é: {nome[0]}')

# print(f'{fim:-^40}')
# print('-' * 40)

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#  descrito, exiba a saudação apropriada. Ex. 
#  Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

# entrada = input('Digite a hora atual: ')

# try:
#     hora = int(entrada)
#     if hora >= 0 and hora <= 11:
#         print('Bom dia.')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde.')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite.')
#     else:
#         print('Não conheço essa hora.')
# except:
#     print('Você não digitou um número inteiro.')

# # Faça um programa que peça ao usuário para digitar um número inteiro,
# #  informe se este número é par ou ímpar. Caso o usuário não digite um número
# #  inteiro, informe que não é um número inteiro.

# num_int = input('Digite um número inteiro: ')

# try:
#     num_int = int(num_int)
#     if num_int % 2 == 0:
#         print('O número é "PAR".')
#     else:
#         print('O número digitado é "IMPAR".')
# except:
#     print('O valor digitado não é INTEIRO!')

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# nome = input('Digite o seu nome: ')
# genero = input('Digite o seu gênero: [F] ou [M]:')

# try:
#     if genero == 'F' or genero == 'f':
#         print(f'A pessoa {nome} é do gênero "FEMININO".')
#     elif genero == 'M' or genero == 'm':
#         print(f'A pessoa {nome} é do gênero "MASCULINO".')
# except:
#     print('A letra digitada é diferente de "F" ou "M".')

# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.
9



# while True:
#         dia_semana = int(input('Digite um número  "de 1 à 7" para saber o dia da semana: '))
#         sair = 0
        
        
#         if dia_semana > 7 or dia_semana < 1:
#             print('Digite um valor válido ou 0 para fechar o programa.')
#         if dia_semana == 0:
#             print('Programa finalizado!')
#             break
            
            
#         elif dia_semana == 1:
#             print('Segunda-feira.')
#         elif dia_semana == 2:
#             print('Terça-feira.')
#         elif dia_semana == 3:
#             print('Quarta-feira.')
#         elif dia_semana == 4:
#             print('Quinta-feira.')
#         elif dia_semana == 5:
#             print('Sexta-feira.')
#         elif dia_semana == 6:
#             print('Sábado.')
#         elif dia_semana == 7:
#             print('Domingo.')
#             break   


# nome = 'Ariclenes Silva'
# print(nome.upper())
# tamanho_nome = len(nome)
# print(tamanho_nome)
# print(nome[0:9])

# indice = 0
# while indice < len(nome):
#     print(nome[indice])
#     indice += 1
                    
        
# import os


# while True:#enquanto essa condição for verdadeira, então faça:
#         nome_do_aluno = input('Digite o nome do aluno ou "sair" para fechar o programa: ')
#         if nome_do_aluno == 'Sair' or nome_do_aluno == 'sair' or nome_do_aluno == 'SAIR':
#             sair = ('Programa finalizado!')
#             print(50 * '-')#vai retornar na tela 50 vezes o traço
#             print(f'{sair:-^50}')
#             break#comando break para a repetição while
#         nota_1 = float(input(f'Digite a nota 1 do aluno {nome_do_aluno}: '))
#         nota_2 = float(input(f'Digite a nota 2 do aluno {nome_do_aluno}: '))
#         nota_3 = float(input(f'Digite a nota 3 do aluno {nome_do_aluno}: '))
#         media = (nota_1+nota_2+nota_3) / 3
        
#         if media >= 7:
#               print(f'O aluno {nome_do_aluno} foi "APROVADO" e sua média foi {media:.2f}!\n{'-'*10}Parabéns!')
#               input('Tecle enter para continuar!')
#               os.system('cls')
#         elif media >= 5:
#               print(f'O aluno {nome_do_aluno} está de "RECUPERAÇÃO" e sua média foi {media:.2f}!')
#               input('Tecle enter para continuar!')
#               os.system('cls')
#         elif media < 5:
#               print(f'O aluno {nome_do_aluno} foi "REPROVADO" e sua média foi {media:.2f}!')
#               input('Tecle enter para continuar!')
#               os.system('cls')


# # criar uma calculadora
# #passo 1: pedir ao usuário que insira um número
# #passo 2: pedir ao usuário que insira outro número
# #passo 3: pedir ao usuário que defina qual operação ele quer fazer
# #passo 4: usar estrutura de repetição
# #passo 5: usar estrutura condicional

# # # criar uma calculadora
# #passo 1: pedir ao usuário que insira um número
# #passo 2: pedir ao usuário que insira outro número
# #passo 3: pedir ao usuário que defina qual operação ele quer fazer
# #passo 4: usar estrutura de repetição
# #passo 5: usar estrutura condicional

# # criar uma calculadora
# #passo 1: pedir ao usuário que insira um número
# #passo 2: pedir ao usuário que insira outro número
# #passo 3: pedir ao usuário que defina qual operação ele quer fazer
# #passo 4: usar estrutura de repetição
# #passo 5: usar estrutura condicional
# import os #importa ações do sistema operacional, como limpar a tela
# import time #importa ações de tempo, como esperar para executar a próxima ação

# while True:#enquanto VERDADEIRO, faça: loop infinito.
    
#     calculadora = 'Calculadora 1.0'#nome do programa
#     print(f'{calculadora:=^40}')#adiciona o item== e deixa o texto centralizado com ^
#     num1 = float(input('Digite um número ou "0" para fechar o programa: '))
#     num2 = float(input('Digite outro número ou "0" para fechar o programa: '))
#     fim = ('Calculadora finalizada!')
  
#     if num1 == 0 or num2 == 0:
#         print(f'{fim:=^40}')
#         break#determina o fim do programa de acordo com a ação do usuário
   
#     operacao = input('Digite qual operação você quer fazer [+, -, *, /]: ')
#     operadores_permitidos = '+-*/'
#     if operacao not in operadores_permitidos:#not in: se não estiverem os caracteres estipulados antes
#         print('Operador inválido!')
#         time.sleep(2)#o programa vai aguardar 2 segundos para executar a próxima ação
#         os.system('cls')#o comando "cls" limpa a tela antes da próxima iteração
#         continue#determina que o código volte ao começo da repetição WHILE

#     if len(operacao) > 1:#len: lê se foi digitado mais de um valor na variável
#         print('Digite apenas um operador!')
#         time.sleep(2)
#         os.system('cls')
#         continue
#     if operacao == '+':
#         # print(num1 + num2)
#         print(f'O resultado da operação {num1} + {num2} é: {num1 + num2:.1f}')
#         input('Aperte enter para continuar')#determina ação do usuário antes de limpar a tela
#         # time.sleep(2)
#         os.system('cls')
       
#     elif operacao == '-':
#         # print(num1 - num2)
#         print(f'O resultado da operação {num1} - {num2} é: {num1 - num2:.1f}')
#         input('Aperte enter para continuar')
#         # time.sleep(2)
#         os.system('cls')
        
#     elif operacao == '*':
#         # print(num1 * num2)
#         print(f'O resultado da operação {num1} * {num2} é: {num1 * num2:.1f}')
#         input('Aperte enter para continuar')
#         # time.sleep(2)
#         os.system('cls')
        
#     else:
#         # print(num1 / num2)
#         print(f'O resultado da operação {num1} / {num2} é: {num1 / num2:.1f}')
#         input('Aperte enter para continuar')
#         # time.sleep(2)
#         os.system('cls')

#fazer um programa que receba uma senha do usuário e compare com a senha salva anteriormente

# import os#importa a biblioteca os(operational system) com comando 'cls' para limpar a tela
# #à cada itereção.
# senha_salva = '123456'#valor da variável recebido previamente
# repeticoes = 1#contador para executar e identificar a quantidade de vezes que foi repetido o loop

# while True:
#     senha_digitada = input('Digite sua senha "NUMÉRICA": ')
#     if senha_digitada != senha_salva and repeticoes == 1:
#         print(f'Você digitou sua senha de forma errada {repeticoes} x.'\
#               ' Você tem mais três tentativas antes de bloquear o sistema!')
#         repeticoes += 1
#         input('Digite ENTER para continuar!')
#         os.system('cls')
      
#     elif senha_digitada != senha_salva and repeticoes == 2:
#         print(f'Você digitou sua senha de forma errada {repeticoes} x.'\
#               ' Você tem mais duas tentativas antes de bloquear o sistema!')
#         input('Digite ENTER para continuar!')
#         os.system('cls')
#         repeticoes += 1
#     elif senha_digitada != senha_salva and repeticoes == 3:
#         print(f'Você digitou sua senha de forma errada {repeticoes} x.'\
#               ' Você tem mais uma tentativa antes de bloquear o sistema!')
#         input('Digite ENTER para continuar!')
#         os.system('cls')
#         repeticoes += 1
        
#     elif senha_digitada != senha_salva and repeticoes >= 3:
#         print('Sua senha foi bloqueada!')
#         break
#     else:
#         print(f'Senha digitada corretamente! Seja bem vindo ao sistema!')
#         break


        
        


