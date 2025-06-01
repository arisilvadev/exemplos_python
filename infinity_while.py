
# soma = 0
# num = 1

# while num <= 10:
#     soma += num
#     num += 1
# print(f'O resultado da soma {soma} é: ')

# Atividade 01:
# Contagem de 1 a 10:
# Crie um programa que use um laço while
# para contar de 1 a 10 e exibir cada número.

# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1

# Atividade 02:
# Soma de Números de 1 a 100:
# Escreva um programa que use um laço while para
# somar os números de 1 a 100 e exiba o resultado.

# soma = 0 
# num = 1

# while num <= 100:
#     soma += num
#     num += 1
#     print(soma)

# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

# num = int(input('Digite um número qualquer para exibir a tabuada: '))
# contador = 0

# while contador <10:
#     contador += 1
#     print(f' o resultado de {num} x {contador} é: {num * contador}')

# Atividade 04:
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir
# uma contagem regressiva de 10 até 1 e, em seguida, exiba
# "Feliz Ano Novo!".
    
# contador = 10
# limite = 0

# while contador > limite:
#     print(f'Contagem regressiva! Faltam {contador} sgundos para o ano novo!')
#     contador -= 1

# #contagem dinâmica(quando se sabe o limite do contador)
# contador = 0
# limite = 10

# while contador <= limite:
#     print(contador)
#     contador += 2

# senha = ''

# while senha != '123456':
#     senha = input('Digite sua senha numérica: ')
#     if senha == '123456':
#         print('Senha correta!')
#     else:
#         print('Senha digitada não confere!')

# atividade 05
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.

# num_inserido = int(input('Digite um número para contar: '))
# contador = 1
# soma = 1

# while contador <= 10:
#     print(f' a soma de {num_inserido} + {soma} é igual à: {num_inserido + soma}')
#     contador += 1
#     soma += num_inserido
    

# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.

# soma = 0

# while True:
#     numero = int(input("Digite um número (negativo para sair): "))
    
#     if numero < 0:
#         break  # Sai do laço se o número for negativo
    
#     soma += numero  # Soma apenas se for positivo
# print(soma)
    

# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.


# numero = int(input("Digite um número para ver a tabuada (apenas resultados múltiplos de 3): "))
# contador = 1

# while contador <= 10:
#     resultado = numero * contador
#     if resultado % 3 == 0:
#         print(f"{numero} x {contador} = {resultado}")
#     contador += 1

# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.

# soma = 0
# repetidor = 0

# while True:
#     nota = float(input("Digite a nota do aluno ou -1 para fechar o programa: "))
    
#     if nota == -1:
#         break  # Sai do laço se o usuário digitar -1
    
#     soma += nota
#     repetidor += 1

# if repetidor > 0:
#     media = soma / repetidor
#     print(f"A média das notas é: {media:.2f}")
# else:
#     print("Nenhuma nota foi inserida.")

# Atividade 09:
# Contagem até 10:
# Crie um programa que use um laço while para contar de 1 a 10
# e termine quando atingir 10.
# contador = 1
# limite = 10

# while contador <= limite:
#     print(contador)
#     contador += 1


# Atividade 10
# Escreva um programa que use um laço while para somar
# números consecutivos começando de 1 e termine quando
# a soma atingir ou ultrapassar 50.

# contador = 1
# limite = 50
# soma = 0

# while contador <= limite:
#     print(f'{soma} + {contador}: {soma}')
#     soma += contador
#     contador += 1
#     if soma > limite:
#         break

# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.

# while True:
#     num = int(input('Digite um número entre 1 e 10: '))
#     if num <= 0 or num > 10:
#         print('Número digitado inválido! Fim do programa!')
#         break

# Atividade 12
# Desenvolva um programa que peça ao usuário para digitar uma
# senha e continue pedindo até que a senha correta (previamente
# definida) seja inserida.


# fim = 'Fim do programa!'

# while True:
#     senha = input('Digite sua senha númerica de SEIS dígitos: ')
#     if senha == '123456':
#         print('Senha correta!')
#         break
# print(f'{fim:=^40}')

#teste de aninhamento de repetições com condicionais:

# while True:
#     print('\nMenu:')
#     print('1. Diga "olá"!')
#     print('2. DIga "bem vindo"!')
#     print('3. Diga "adeus"!')
#     opcao = input('Digite uma opção de 1 à 3: ')

#     if opcao == '1':
#         print('Olá!')
        
#     elif opcao == '2':
#         print('Bem vindo!')
#     elif opcao == '3':
#         print('Adeus!')
#     else:
#         print('Nenhuma condição válida foi inserida!')

# DESAFIOS

# 1 - Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.

# numero = 1
# soma_pares = 0

# while numero <= 100:
#     if numero % 2 == 0:
#         soma_pares += numero
#     numero += 1

# print("A soma de todos os números pares de 1 a 100 é:", soma_pares)


# 2 - Números Ímpares de 1 a 50:
# Escreva um programa que use um laço while
# para exibir todos os números ímpares de 1 a 50.

# numero = 1

# while numero <= 50:
#     if numero % 2 != 0:
#         print(numero, end= " ")
#     numero += 1

# Faça um programa que use um laço while para exibir os
# primeiros 20 termos da sequência de Fibonacci.
# a = 0
# b = 1
# contador = 0

# while contador < 20:
#     print(a, end=" ")
#     # Próximo termo é a soma dos dois anteriores
#     proximo = a + b
#     a = b
#     b = proximo
#     contador += 1


# DESAFIO 05
# Desenvolva um jogo de adivinhação onde o
# programa escolhe um número aleatório entre 1 e
# 100. O usuário deve tentar adivinhar o número, e
# o programa deve fornecer dicas se o palpite está
# muito alto ou baixo.

# import random
# import os

# numero_aleatorio = random.randint(1, 100)
# tentativa = 0
# palpite = None
# fim = 'Fim do jogo!'
# titulo = '🍀 Jogo da adivinhação 🍀'

# while palpite != numero_aleatorio:
#     try:
   
#         print(f'{titulo:^40}')
#         palpite = int(input('🤔 tente adivinhar o número sorteado: '))
#         tentativa += 1
#         # if tentativa > 3:
#         #     print('Você excedeu o número de tentativas!')
#         #     print(fim)
#         #     break
        
#         if palpite < numero_aleatorio:
#             print('😡 O número digitado está ABAIXO do número sorteado!')
#             input('Digite "enter" para tentar outra novamente!')
#             os.system('cls')
#         elif palpite > numero_aleatorio:
#             print('😡 O número digitado está ACIMA do número sorteado! Tente novamente!')
#             input('Digite "enter" para tentar novamente!')
#             os.system('cls')
#         else:
#             print(f'✅️ Parabéns! Você acertou o número sorteado em {tentativa} tentativas!')
#     except:
#         print('Por favor, digite apenas números inteiros!')
#         input('Digite "enter" para continuar!')
#         os.system('cls')

     
# print(f'{fim:=^40}')
    
     
#DESENVOLVER UM CÓDIGO QUE SORTEI NÚMEROS ALEATÓRIOS PARA A MEGA SENA

# import random


# contador = 1
# titulo = '☘️  NÚMEROS DA SORTE ☘️'
# print(f'{titulo:=^30}')
# fim = 'Fim do programa!😉 Boa sorte!'


# while True:
#     numeros_sorteados = random.randint(1,60)
#     if numeros_sorteados <= 60:
#             print(numeros_sorteados, end=' ')
#     contador += 1
#     if contador > 6:
#         print(f'\n{fim:=^40}')
#         break
   
    
    


