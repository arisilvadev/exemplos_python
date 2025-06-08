
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

dicionario = {
    'nome':'ari',
    'cidade':'recife',
    'idade':'37'
}
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
print(list(iter(dicionario)))# tem o mesmo resultado de chave.keys


# %%