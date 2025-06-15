
#MATERIAL DA AULA DE DICIONÁRIOS E SETS DA INFINITY SCHOOL
# convidados = {'João', 'Maria', 'Eduarda'}
# print(convidados)
# convidados.add('Marcela')#usando o método add() para adicionar itens ao set
# print(convidados)
#------------------------------------------------------------------
# %% MÉTODO UPDATE PARA ADICIONAR ITENS DE OUTRO CONJUNTO
#usando o update() para adicionar itens de outro conjunto ao set especificado
# set1 = {'ari', 'chico', 'carro'}
# set2 = {'carla', 'dinheiro', 'cachorro'}
# print(set1)
# set1.update(set2)
# print(set1)
#-------------------------------------------------------------------
# %% COMO ENCONTRAR UM ITEM DENTRO DE UM CONJUNTO
#OBS: sets não permitem uso de índice para encontrar o item em questão
# nomes = {'maria', 'joão', 'ari'}

# print('maria' in nomes)

# #ou

# for i in nomes:
#     print(i)
#--------------------------------------------------------------------
# %% MÉTODOS REMOVE E DISCARD PARA EXCLUIR UM ITEM DO CONJUNTO
#usando remove() e discard() para remover um item do conjunto:
# nomes = {'maria', 'joão', 'ari'}
# print(nomes)
# nomes.remove('maria')#REMOVE: se o elemento não existir na lista, ele gera um erro
# print(nomes)
# nomes.discard('ari')#DISCARD: se o elemento não existir na lista, ele não faz nada
# print(nomes)
#--------------------------------------------------------------------
# %% MÉTODO INTERSECTION PARA RETORNAR VALORES IGUAIS EM DIFERENTES CONJUNTOS
#usando o método intersection() para retornar valores iguais contidos em mais de um conjunto(set):

# convidados1 = {'ari', 'carlos', 'maria'}
# print(convidados1)
# convidados2 = {'joão', 'carlos', 'maria'}
# print(convidados2)
# print(convidados1.intersection(convidados2))
#saida: 'maria'
#----------------------------------------------------------------------
# %% MÉTODO UNION PARA UNIR CONJUNTOS
#usando o método union() para retornar um conjunto de elementos de ambos os sets sem repetições:

# convidados1 = {'ari', 'carlos', 'maria'}
# print(convidados1)
# convidados2 = {'joão', 'carlos', 'maria'}
# print(convidados2)
# print(convidados1.union(convidados2))
#saída: 'joão', 'carlos', 'maria', 'ari'

#-----------------------------------------------------------------------
# %% atividade 01
#ATIVIDADE PRÁTICA 1

# Crie um conjunto vazio chamado frutas e adicione as
# seguintes frutas a ele:
# 'maçã', 'banana', 'uva', 'laranja', 'morango'.
# Em seguida, imprima o conjunto;

# frutas = set()#set() cria um conjunto vazio em sets

# frutas2 = {'maçã', 'banana', 'uva', 'laranja', 'morango'}

# frutas.add('limão')#add adiciona um item por vez
# print(frutas)
# frutas.update(frutas2)#update adiciona vários itens ao mesmo tempo
# print(frutas)
#----------------------------------------------------------------
# %% atividade 02
#ATIVIDADE PRÁTICA 2

# Verifique se a fruta "banana" está presente no conjunto
# frutas e imprima o resultado.
# frutas2 = {'maçã', 'banana', 'uva', 'laranja', 'morango'}
# frutas2.discard('banana')#retira o elemento do conjunto sem dar erro
# print('banana' in frutas2)

# #ou

# if 'banana' in frutas2:
#     print('A fruta "banana" está no conjunto.')
# else:
#     print('A fruta não está no conjunto!')
#------------------------------------------------------------
# %% atividade 03
#ATIVIDADE PRÁTICA 3

# Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele:
# 'morango', 'cereja' e 'framboesa'. Em seguida, imprima o conteúdo:

# frutas_vermelhas = set()

# frutas_vermelhas.add('morango')
# frutas_vermelhas.add('cereja')
# frutas_vermelhas.add('framboesa')

# print(f'{frutas_vermelhas} são frutas vermelhas!')
# for i in frutas_vermelhas:
#     print(i)
#-------------------------------------------------------------------
# %% atividade 04
#ATIVIDADE PRÁTICA 4

# Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

# frutas_vermelhas = set()

# frutas_vermelhas.add('morango')
# frutas_vermelhas.add('cereja')
# frutas_vermelhas.add('framboesa')

# print(f'{frutas_vermelhas} são frutas vermelhas!')
# for i in frutas_vermelhas:
#     print(f'"{i}"')
# frutas_vermelhas.discard('cereja')
# print(f'{frutas_vermelhas} lista atualizada!')
# for i in frutas_vermelhas:
#     print(f'"{i}"')
#-----------------------------------------------------------
# %% atividade 05
#ATIVIDADE PRÁTICA 5

# Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

# nomes_1 = {'ari', 'chico', 'joão'}
# nomes_2 = {'maria', 'antônio', 'marcela'}
# print(nomes_1)
# print(nomes_2)

# print(nomes_1.union(nomes_2))
#------------------------------------------------------------------------
# %% atividade 06
#ATIVIDADE PRÁTICA 6

# Crie um programa que recebe dois conjuntos e exibe a interseção deles.

# nomes_1 = {'ari', 'chico', 'joão', 'maria'}
# nomes_2 = {'maria', 'antônio', 'marcela'}
# print(nomes_1)
# print(nomes_2)

# print(f'O nome que se repete é: ', nomes_1.intersection(nomes_2))
#---------------------------------------------------------------------
# %% atividade 07
#ATIVIDADE PRÁTICA 7

# Escreva um programa que receba duas listas e calcule
# a união dos elementos únicos dessas listas, usando conjuntos.
# Duas listas de exemplo

# lista1 = [1, 2, 3, 4, 5, 5]
# lista2 = [4, 5, 6, 7, 8]
# print(lista1 + lista2)

# # Converte as listas em conjuntos para MANTER APENAS ELEMENTOS ÚNICOS(principal função dos conjuntos)
# conjunto1 = set(lista1)
# conjunto2 = set(lista2)

# # Calcula a união dos dois conjuntos
# uniao = conjunto1.union(conjunto2)

# # Exibe o resultado
# print("União dos elementos sem repetição:", uniao)
# %% INÍCIO DA AULA DE DICIONÁRIOS:

# dicionario = {
#     'animal': 'chico',#animal, tutor e raça são as chaves e chico, ari e pug, são os valores do dicionário
#     'tutor': 'ari silva',
#     'raça': 'pug'
# }


# print(dicionario)
# print(type(dicionario))

# %% USANDO CONSTRUTOR DICT():

# dicionario = dict()#dicionário vazio
# dicionario = dict([('Módulo', 'Python'), ('Intituição', 'Infinity School')])
# print(dicionario)
#-----------------------------------------------------------------------------------

# %% USANDO O .ITEMS() E ACESSANDO UM VALOR DENTRO DO DICIONÁRIO:
# carros = {
#     'Hiunday':'HB20',#hiunday é a chave e o hb20 (modelo) é o valor
#     'Chevrolet':'Onix',#chevrolet é a chave e o onix é o valor
#     'Fiat':'Mobi'
# }

# for i in carros.items():
#     print(i)

# print(carros['Fiat'])#usando colchetes e apas para acessar um valor específico do dicionário
# print(carros['Chevrolet'])
# print(carros.get('Hiunday'))#outro meio de acessar um valor dentro do dicionário

# %% ATIVIDADE PRÁTICA 08:
# Escreva um programa que EXIBA um dicionário contendo
# informações de pessoas (nome, idade) e exiba essas informações.

# cadastro_pessoas = {
#     'Ari Silva':'37',
#     'Chico Pug':'5',
#     'José Antônio':'50'
# }

# for i in cadastro_pessoas.items():#.items retorna uma view de todos os itens  em forma de tupla
#     print(i)
#-----------------------------------------------------------------------------------

# %% ATIVIDADE PRÁTICA 09:

# Escreva um programa que percorra as chaves e valores de um 
# dicionário separadamente e os exiba.

# dados = {
#     "nome": "Ari Silva",
#     "idade": 37,
#     "cidade": "Recife"
# }

# # Percorrendo e exibindo apenas as chaves
# print("Chaves do dicionário:")
# for chave in dados.keys():#.keys exibe apenas as chaves do dicionário
#     print(chave)

# # Percorrendo e exibindo apenas os valores
# print("\nValores do dicionário:")
# for valor in dados.values():#.values exibe apenas os valores do dicionário
#     print(valor)

# %% OPERAÇÕES DENTRO DO DICIONÁRIO:

# dicionario = {
#     'nome':'ari',
#     'cidade':'recife',
#     'idade':'37'
# }
# print(list(dicionario))#retorna uma lista com todas as chaves do dicionário
# print(len(dicionario))#retorna o número de itens do dicionário
# print(dicionario['idade'])#retorna o valor da chave especificada
# del dicionario['cidade']#remove a chave e seu respectivo valor do dicionário
# print(dicionario)
# dicionario['cidade'] = 'olinda'#sobreescreve ou cria uma chave e valor
# print(dicionario)
# if 'nome' in dicionario:#chave in dicionário para verificar se a chave está contida no dicionário
#     print(f'A chave "nome" se encontra no dicionário!')
# if 'região' not in dicionario:
#     print('A chave "região" NÃO se encontra no dicionário!')
# print(list(iter(dicionario)))# tem o mesmo resultado de chave.keys


# %% ATIVIDADE PRÁTICA 10:
# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já existir.

 
# dicionario = {}#criando um dicionário vazio 

# while True:
   
#     chave = input('Digite a chave que deseja adicionar ou [s] para sair: ')
#     if chave == 's':#estrutura condicional de parada
#         break
#     valor = input('Digite o valor que deseja adicionar ou [s] para sair: ')
#     if valor == 's':
#         break
    
#     dicionario[chave] = valor #subscreve ou adiciona uma chave e um valor
#     print(dicionario, end='\n\n')

# %% ATIVIDADE PRÁTICA 11
# Escreva um programa que recebe um dicionário e uma
# lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso contrário.

# dicionario = {
#     'Nome':'Ari',
#     'Idade': '37',
#     'Cidade':'Recife',
#     'País':'Brasil'
# }

# chaves = ['Nome', 'Idade', 'Cidade', 'País', 'Religião']


# resultado = all(chave in dicionario for chave in chaves)#função all retorna True se todos os testes
#                                                         #forem verdadeiros.
# print(resultado)

#OU USANDO FUNÇÃO: 

def verifica_chaves(dicionario, chaves):
    for chave in chaves:
        if chave not in dicionario:
            return False
    return True

dicionario = {
'nome':'ari',
'idade':37,
'cidade':'recife'
}

chaves = ['nome', 'idade', 'cidade']

resultado = verifica_chaves(dicionario, chaves)
print(resultado)
#-------------------------------------------------------------------------
# %% ATIVIDADE PRÁTICA 12
#Crie um programa que simule um sistema de votação. O
# programa deve permitir que os eleitores escolham entre
# opções de CANDIDATOS e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da
# votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa
# somente se o usuário digitar o número 0 e exiba os
# resultados finais.

#EXEMPLO 01-----------
# votacao = {
#     'Ari': 0,
#     'Chico': 0,
#     'Maria': 0
# }
# votos = (0)
# votos1 = (0)
# votos2 = (0)
# votos3 = (0)
# canditato01 = (0)
# canditato02 = (0)
# canditato03 = (0)


# while True:
#     opcao = input('Escolha entre os candidatos [1] Ari, [2] Chico, [3] Maria, ou [0] para sair: \n')
#     if opcao == '0':
#         print('Contagem geral de votos: ')
#         print(f'O candidato Ari teve {canditato01} votos.')
#         print(f'O candidato Chico teve {canditato02} votos.')
#         print(f'O candidato Maria teve {canditato03} votos.')
#         print(f'Quantidade total de votos: {votos}')
#         print(votacao)
        
#         if canditato01 > canditato02 and canditato03:
#             print('O candidato Ari é o vencedor da eleição.')
#         elif canditato02 > canditato01 and canditato03:
#             print('O candidato Chico é o vencedor da eleição.')
#         else:
#             print('O candidato Maria é o vencedor da eleição.')
        
#         break
    
#     elif opcao == '1':
#         canditato01 += 1
#         votos1 += 1
#         votacao['Ari'] = votos1
        
#     elif opcao == '2':
#         canditato02 += 1
#         votos2 += 1
#         votacao['Chico'] = votos2
        
#     elif opcao == '3':
#         canditato03 += 1
#         votos3 += 1
#         votacao['Maria'] = votos3

#EXEMPLO 02-------------
# votos = {
#     1: 0,  # Candidato 1
#     2: 0,  # Candidato 2
#     3: 0   # Candidato 3
# }

# print("Sistema de Votação\n")
# print("Digite o número do candidato:")
# print("1 - Candidato A")
# print("2 - Candidato B")
# print("3 - Candidato C")
# print("0 - Encerrar votação")

# while True:
#     voto = input("Seu voto: ")
    
#     if voto == '0':
#         break
#     elif voto in ['1', '2', '3']:
#         votos[int(voto)] += 1
#     else:
#         print("Opção inválida. Tente novamente.")

# # Exibindo resultados
# print("\nRESULTADOS FINAIS:")
# print(f"Candidato A: {votos[1]} votos")
# print(f"Candidato B: {votos[2]} votos")
# print(f"Candidato C: {votos[3]} votos")

#EXEMPLO 3:
# votacao = {
#     'Ari': 0,
#     'Chico': 0,
#     'Maria': 0
# }

# while True:
#     opcao = input('Escolha entre os candidatos [1] Ari, [2] Chico, [3] Maria, ou [0] para sair: \n')

#     if opcao == '0':
#         total_votos = sum(votacao.values())
#         print('\nContagem geral de votos:')
#         print(f"O candidato Ari teve {votacao['Ari']} votos.")
#         print(f"O candidato Chico teve {votacao['Chico']} votos.")
#         print(f"O candidato Maria teve {votacao['Maria']} votos.")
#         print(f"Quantidade total de votos: {total_votos}")
#         print(votacao)

#         vencedor = max(votacao, key=votacao.get)#get para acessar o valor e key(parâmetro) 
#                                                 #para dizer como o max vai agir
#                     #max é função para descobrir qual teve mais votos
#         print(f'O candidato {vencedor} é o vencedor da eleição.')
#         break

#     elif opcao == '1':
#         votacao['Ari'] += 1
#     elif opcao == '2':
#         votacao['Chico'] += 1
#     elif opcao == '3':
#         votacao['Maria'] += 1
#     else:
#         print("Opção inválida. Tente novamente.")
#---------------------------------------------------------------------------
# %% ATIVIDADE PRÁTICA 13:
# Crie um dicionário que relacione nomes de alunos às suas
# notas em uma disciplina. Calcule a média das notas eexiba-a.
    
# notas = {
#     'Ari': 8.6,
#     'Chico': 9.4,
#     'Maria': 8.5
# }

# soma = sum(notas.values())

# quantidade = len(notas)

# media = soma / quantidade

# print(f'A média das notas é: {media:.2f}')
#------------------------------------------------------
# %% ATIVIDADE PRÁTICA 14:
# Crie um programa que receba uma lista de números e
# remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.

# numeros = [
#     1,2,3,4,4,5,1,6,7,7,8
# ]

# numeros_att = set(numeros)
# print(numeros)
# print(numeros_att)
#--------------------------------------------------------------

# %% ATIVIDADE PRÁTICA 15:
# Crie um programa que realize a união de múltiplos
# conjuntos e exiba o conjunto resultante.

# conjunto = set()

# frutas = {
#     'Maçã', 'Banana', 'Laranja'
# }

# legumes = {
#     'Cenoura', 'Vagem', 'Quiabo'
# }

# temperos = {
#     'Sal', 'Cominho', 'Pimenta'
# }

# conjunto_total = frutas.union(legumes, temperos)

# print(conjunto_total)
#---------------------------------------------------------------

# %% DESAFIO PRÁTICO 01:
# Sistema de Cadastro de Alunos - passo 1

# Cadastro de Alunos: O programa deve permitir ao usuário
# cadastrar alunos. Cada aluno terá as seguintes
# informações: nome, idade e notas em três disciplinas:
# Matemática, Ciências e História. Os dados de cada aluno
# devem ser armazenados em um dicionário com as
# seguintes chaves:'nome','idade','notas'. As notas devem
# ser armazenadas em uma tupla.

# alunos = []

# while True:
#     nome = input('Digite o nome do aluno ou [0] para sair: ')
#     if nome == '0':
#         break
    
#     idade = int(input('Digite a idade do aluno: '))
#     matematica = float(input('Digite a nota em matemática: '))
#     ciencias = float(input('Digite a nota em ciências: '))
#     historia = float(input('Digite a nota em história: '))
    
#     notas = (matematica, ciencias, historia)
    
#     dic_alunos = {
#         'Nome': nome,
#         'Idade': idade,
#         'Notas': notas
#     }
    
#     alunos.append(dic_alunos)

# print('\nAlunos cadastrados:')
# maior_media = -1#menor valor de comparação, já que média começa em 0
# melhor_aluno = None#classifica o aluno com maior média

# for aluno in alunos:
#     notas = aluno['Notas']
#     media = sum(notas) / len(notas)
#     print(f"O aluno {aluno['Nome']} obteve as notas {notas} e média de {media:.2f}")
    
#     if media > maior_media:#se a média for maior que -1
#         maior_media = media#-1 passa à ter o valor da média atual e maior
#         melhor_aluno = aluno['Nome']#melhor aluno que era None passa a ser o aluno da lista

# print(f'\nAluno com a maior média: {melhor_aluno} ({maior_media:.2f})')
    
#Sistema de Cadastro de Alunos - passo 2

# Visualização de Alunos: O programa deve permitir ao usuário
# visualizar todos os alunos cadastrados, exibindo suas informações
# de forma organizada.
# Média de Notas: O programa deve calcular a média das
# notas de cada aluno e exibi-la.
# Aluno com Melhor Média: O programa deve identificar e
# exibir o aluno com a melhor média de notas.
#---------------------------------------------------------------

# %% EXERCÍCIO CRIADO 01:
# Questão 1: Criação de Dicionário
# Crie um dicionário chamado aluno com as chaves 'nome', 'idade' e 'curso'. 
# Atribua valores a essas chaves que representem um aluno fictício.

# aluno = {
#     'Nome': 'Ari',
#     'Idade': 37,
#     'Curso': 'Python'
# }
# print(aluno)



#Questão 2: Acesso a Valores
# Acesse e imprima o valor associado à chave 'curso' do dicionário aluno que você criou.
# print(aluno['Curso'])
# for i in aluno:
#     print(i)

# #Questão 3: Adição de Chave-Valor
# # Adicione uma nova chave 'cidade' ao dicionário aluno e atribua o valor 'Recife' a ela.

# aluno['Cidade'] = 'Recife'
# print(aluno)
# aluno['Cidade'] = 'Olinda'
# print(aluno)

