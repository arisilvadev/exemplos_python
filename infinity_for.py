
# Atividade 01:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

# while True:
#     num = int(input(' 👉  Digite um número para a tabuada: '))

#     for iteravel in range(1,11):
#         print(f'{iteravel} x {num} é igual à: {iteravel * num}')
#         continue

# Atividade 02:
# Soma de Números de 1 a 100:
# Crie um programa que use um laço for para somar
# todos os números de 1 a 100 e exiba o resultado.

# soma = 1
# fim = '  Até a próxima 🖐  '

# for num in range(1,100):
#     print(f' {num} + {soma} é igual à : {num + soma}')
#     soma += 1
# print(f'{fim:=^30}')

# Atividade 03:
# Caractere por Caractere:
# Escreva um programa que solicite uma palavra ao usuário e use um
# laço for para exibir cada caractere da palavra em uma linha separada.

# while True:
#     palavra = input('Digite uma palavra qualquer: ')
#     for letra in palavra:
#         print(f'{letra:>2} \n ╰┈➤.')
#         continue

# Atividade 04:
# Contagem Regressiva de 10 a 1:
# Desenvolva um programa que use um laço for para fazer uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

# import time
# ano_novo = input('Digite enter para a contagem regressiva!')

# for numero in range(10,0,-1):
#     print(f'Faltam {numero} segundos para o ano novo!')
#     time.sleep(1)
# print(' 😍 Feliz ano novo!🥰 ')


# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.

# positivos = 0
# negativos = 0

# for i in range(10):
#     numero = float(input(f"Digite o {i + 1}º número: "))
    
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
    

# print(f"\nTotal de números positivos: {positivos}")
# print(f"Total de números negativos: {negativos}")

# Atividade 06:
# Soma de Números Pares:
# Escreva um programa que use um laço for para somar
# todos os números pares de 1 a 50 e exiba o resultado final.

# soma = 0

# for i in range(1,51):
#     if i % 2==0:
#         print(f'A soma de {i} + {soma} é igual à: {i + soma}!')
#         soma += i

# Atividade 07:
# Contagem de Vogais em uma Palavra:
# Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.


# palavra = input("Digite uma palavra: ").lower()  
# vogais = "aeiou"
# contador = 0

# for letra in palavra:
#         if letra in vogais:
#             contador += 1

# print(f"A palavra '{palavra}' contém {contador} vogal(is).")

# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6

# # "Reprovado" para média < 6).
# import time
# import os
# nota = 0
# soma = 0
# media = 0


# while True:
#     aluno = input('Digite o nome do aluno ou [s] para sair: ').lower()
#     while not all(parte.isalpha() for parte in aluno.split()):#.split divide a string em partes com o espaço
#                                                             #.isalpha verifica se cada palavra tem apenas letras
#         #not all vai entrar no laço se alguma palavra não for apenas letras.
#         print("Entrada inválida! Digite apenas letras, sem números ou símbolos.")
#         aluno = input("Tente novamente: ")
#         continue

#     if aluno == 's':
#           print(' ❌ Fim do programa! ❌ ')
#           break
#     for i in range(0,5):
#         nota = float(input(f'Digite a {i + 1}ª nota do aluno {aluno}: '))
#         soma += nota
#         media = soma / 5
#         continue
#     if media >= 6:
#             print(f'✅ O aluno {aluno} está aprovado com média igual à: {media:.2f}.!')
#             time.sleep(2)
#             input('Digite "enter" para continuar!')
#             os.system('cls')
#     else:
#             print(f'❗ O aluno {aluno} está reprovado com média igual à: {media:.2f}.!')
#             time.sleep(2)#o programa espera 2 segundos para executar a próxima linha
#             input('Digite "enter" para continuar!')#faz o programa esperar uma ação do usuário
#             os.system('cls')#executa a limpeza do terminal

# Atividade 09:
# Verificar Números Pares e Impares com Interrupção:
# Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
# identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

# for i in range(1,20):
#     if i == 15:
#         print('Número 15 encontrado! Parando o programa!')
#         break
#     if i % 2 == 0:
#         print(f'O número {i} é PAR!')
#     else:
#         print(f'O número {i} é ÍMPAR!')

# Atividade 10:
# Contar Números Positivos e Negativos:
# Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
# são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.

# num_positivos = 0
# num_negativos = 0

# for i in range(10):
#     numero = float(input(f'Digite o {i + 1} º número ou 0 para sair: '))
#     if numero == 0:
#         print('Número "0" encontrado. Saindo do programa!')
#     elif numero > 0:
#         num_positivos += 1
#     elif numero < 0:
#         num_negativos += 1
# print(f'Total de números positivos encontrados: {num_positivos}')
# print(f'Total de números negativos encontrados: {num_negativos}')

# Atividade 11:
# Verificar Múltiplos de 5 e Parar:
# Escreva um programa que use um laço for para imprimir números de 1 a 30.
# Use uma condicional para verificar se um número é múltiplo de 5 e outro
# para verificar se é maior que 20 e interromper o loop com break.

# for numero in range(1, 31):  # De 1 até 30 porque o python não mostra o último número
#     print(f"Número: {numero}")
    
#     if numero % 5 == 0:
#         print("✅ É múltiplo de 5!")

#     if numero > 20:
#         print("❌ Número maior que 20. Encerrando o loop.")
#         break
    
# Atividade 12:
# Soma de Números com Desconto:
# Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.

# total = 0

# for i in range(5):
#     preco = float(input(f"Digite o preço do {i + 1}º produto: "))
#     total += preco
#     print(f'Valor antes do desconto: {total}')

#     if total > 100:
#         print("Total ultrapassou R$100. Aplicando desconto de 10% e encerrando.")
#         total *= 0.9  # Aplica 10% de desconto
#         break

# print(f'Valor com desconto: R$ {total}')


    


