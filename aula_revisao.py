# %% AULA DE REVISÃO - ATIVIDADE PRÁTICA 01:
#Peça a idade do usuário com base na idade fornecida, o programa deve
# classificar a pessoa em uma das seguintes categorias:
# Se a idade for menor que 12 anos, imprimir "Criança".
# Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente".
# Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto".
# Se a idade for igual ou superior a 60 anos, imprimir "Idoso".


# while True:
#     entrada = input('Digite a idade do usuário ou [s] para sair: ')
    
#     if entrada.lower() == 's':
#         print('Saindo do programa!')
#         break

#     try:#tenta converte str para int e se o valor não for int(ab-*) trata o erro com o except
#         idade_usuario = int(entrada)#transformar str em inteiro (número) para ser aceito
#         if idade_usuario < 12:
#             print('O usuário é UMA CRIANÇA!')
#         elif 12 <= idade_usuario <= 17:#maior igual à 12(número antes dos sinais) e menor igual à 17
#             print('O usuário é UM ADOLESCENTE!')
#         elif 18 <= idade_usuario <= 59:
#             print('O usuário é UM ADULTO!')
#         else:
#             print('O usuário é UM IDOSO!')
#     except ValueError:
#         print('Digite uma idade válida ou "s" para sair.')
#-----------------------------------------------------------------------------------------------
        
# %% AULA DE REVISÃO - ATIVIDADE PRÁTICA 02:
# Faça um programa que leia 3 números e informe o maior número e o menor.

# numeros = []

# for i in range(1,4):
#     while True:
#         try:#usando para garantir que o usuário insira um número e não sinais ou letras
#             numero = float(input(f'Digite o {i}º número: '))
#             numeros.append(numero)
#             break
#         except ValueError:
#             print('Digite um número válido!')
    
# maior_num = max(numeros)
# menor_num = min(numeros)

# print(f'\nO maior número é {maior_num:.0f}.')
# print(f'\nO menor número é {menor_num:.0f}.')
#--------------------------------------------------------------------------

# %% AULA DE REVISÃO - ATIVIDADE PRÁTICA 03:
#Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

# numeros = []
# num_par = 0
# num_impar = 0
# pares = []
# impares = []

# for i in range(1, 11):
#     while True:#laço para repetir a validação de NÚMERO
#         try:#validar que o usuário digite apenas números
#             numero = int(input(f'Digite o {i}º número: '))
#             numeros.append(numero)
            
#             if numero % 2 == 0:
#                 num_par += 1
#                 pares.append(numero)
#             else:
#                 num_impar += 1
#                 impares.append(numero)
            
#             break  # Sai do while se a entrada for válida
#         except ValueError:#trata o erro e exibe a mensagem abaixo, para não estourar na tela
#             print('Digite um número válido!')

# soma_numeros = sum(numeros)
# print(f'\n👉​ A soma dos números inseridos é: {soma_numeros}')
# print(f'\n✔️ ​ Os números PARES são: {pares} e a quantidade: {num_par}')
# print(f'\n✔️  ​Os números ÍMPARES são: {impares} e a quantidade: {num_impar}')
#------------------------------------------------------------------------------

# %% AULA DE REVISÃO - ATIVIDADE PRÁTICA 04:
# Faça um programa que peça para n pessoas a sua
# idade, ao final o programa devera verificar se a média
# de idade da turma varia entre 0 e 25, 26 e 60 e maior
# que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.

# pessoas = int(input("Digite a quantidade de pessoas que irão contar a idade: "))
# soma_idades = 0

# for i in range(pessoas):
#     idade = int(input(f"Idade da {i + 1}ª pessoa: "))
#     soma_idades += idade

# media = soma_idades / pessoas
# print(f"Média de idade: {media:.1f}")

# if media <= 25:
#     print("Turma JOVEM")
# elif media <= 60:
#     print("Turma ADULTA")
# else:
#     print("Turma IDOSA")
#-----------------------------------------------------

# %% AULA DE REVISÃO - ATIVIDADE PRÁTICA 05:
# Faça um programa que, dado um conjunto de N
# números, determine o menor valor, o maior valor e a
# soma dos valores.

# numeros = []

# while True:
#     numero = input("Digite um número (ou 'sair' para encerrar): ")
#     if numero.lower() == 'sair':
#         break
#     try:
#         numeros.append(float(numero))
#     except:
#         print("Número inválido.")

# if numeros:
#     print(f"Menor número inserido: {min(numeros):.0f}")
#     print(f"Maior número inserido: {max(numeros):.0f}")
#     print(f"Soma de todos os números inseridos: {sum(numeros):.0f}")
# else:
#     print("Nenhum número válido foi informado.")
#------------------------------------------------------------------------------

# %% AULA DE REVISÃO - DESAFIO PRÁTICO:

# Gerenciamento de Compras de Produtos

# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra,

# incluindo:

# A) O total gasto na compra.

# B) A quantidade de produtos que custam mais de R$1000.

# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.


lista_compras = {}
total_gasto = 0
mais_1000 = 0

while True:
    produto = input('Digite o nome do produto para adicionar: ')
    try:
        preco = float(input('Digite o preço do produto adicionado: '))
    except ValueError:
        print('Valor digitado inválido. Digite números!')
        continue

    lista_compras[produto] = preco
    total_gasto += preco
    
    if preco > 1000:
        mais_1000 += 1
    
    continuar = input('Deseja adicionar outro produto? [s] para sim ou [n] para não: ')
    if continuar != 's':
        break
    
mais_barato_produto = min(lista_compras, key=lista_compras.get)
mais_barato_preco = lista_compras[mais_barato_produto]

print('\n====Lista de Compras====')
for produto, preco in lista_compras.items():
    print(f'- {produto}: R$ {preco:.2f}')


print(f'O total gasto na lista é de: {total_gasto}')
print(f'Produtos acima de 1000 reais: {mais_1000}')
print(f'O produto mais barato da lista é: {mais_barato_produto} (R$ {mais_barato_preco:.2f})')
#-----------------------------------------------------------------------------------------

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = []

while True:
    print('\nLista de compras!')
    print('Escolha, abaixo, uma opção: ')
    opcao = input('[i] inserir, [a] apagar, [e] exibir ou [s] para sair: ').lower()

    if opcao == 's':
        print('Encerrando a lista de compras!')
        break

    elif opcao == 'i':
        produto = input('Digite o nome do produto para adicionar: ')
        if produto:
            lista_compras.append(produto)
            print(f'Produto {produto} adicionado com sucesso!')
        else:
            print('O item não pode estar vazio. Digite o produto!')
            input('Aperte ENTER para continuar!')

    elif opcao == 'a':
        if not lista_compras:
            print('Lista vazia.')
            continue

        for i, valor in enumerate(lista_compras):
            print(f'{i + 1}. {valor}')

        try:
            indice_produto = input('Digite o número do produto que deseja apagar: ')
            indice_inteiro = int(indice_produto)
            indice = indice_inteiro - 1
            if 0 <= indice < len(lista_compras):
                indice_removido = lista_compras.pop(indice)
                print(f'Produto {indice_removido} removido com sucesso!')
            else:
                print('Índice digitado inválido!')
        except ValueError:
            print('Digite um número inteiro!')

    elif opcao == 'e':
        if not lista_compras:
            print('Lista está vazia.')
        else:
            print('Itens na lista de compras:')
            for i, item in enumerate(lista_compras):
                print(f'{i + 1}. {item}')

    else:
        print('Opção inválida. Tente novamente.')