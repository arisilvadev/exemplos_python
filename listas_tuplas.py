# nomes = [
#     ('ari silva', 38),
#     ('maria lago', 43),
#     ('chico pug', 5)
# ]

# ordenado = sorted(nomes, key=lambda x: x[1])
# for item in ordenado:
#     print(item)
#------------------------------------------
# def calcular_media(lista):
#     return sum(lista) / len(lista)

# notas = [7, 8, 9]
# media = calcular_media(notas)
# print(f"Média: {media:.2f}")
#------------------------------------------
# nomes = ["joão", "maria", "ana", "Carlos"]

# # Ordenar com base no tamanho do nome
# nomes_ordenados = sorted(nomes, key=len)
# print(nomes_ordenados)

#------------------------------------------------------


# alunos = [
#     ('Ari Silva', 9.8, 8.0, 7.5),
#     ('Maria Lago', 6.5, 8.0, 7.5),
#     ('Chico Pug', 9.8, 4.7, 9.5)
# ]

# # Lista para armazenar (nome, média)
# medias = []

# for aluno in alunos:
#     nome = aluno[0]
#     notas = aluno[1:]
#     media = sum(notas) / len(notas)
#     medias.append((nome, media))

# # Ordenar pela média (do maior para o menor)
# medias.sort(key=lambda x: x[1], reverse=True)

# # Mostrar resultados
# for nome, media in medias:
#     print(f'{nome}: Média = {media:.2f}')

#  EXERCÍCIO DE FIXAÇÃO DE LISTAS
# Crie uma lista com 5 nomes de frutas e exiba a lista.

# frutas = ['maçã', 'uva', 'goiaba', 'abacaxi', 'melão']
# print(frutas)
# # Adicione uma nova fruta ao final da lista.
# frutas.append('pinha')
# print(frutas)
# #Insira uma fruta na segunda posição da lista.
# frutas.insert(1, 'banana')
# print(frutas)
# #Remova uma fruta da lista pelo nome.
# frutas.remove('banana')
# print(frutas)
# #Acesse e exiba o terceiro item da lista.
# print(frutas[2])
# #Verifique se a fruta "maçã" está na lista.
# if 'maçã' in frutas:
#     print('O item "maçã" está na lista!')
# else:
#     print('O item "maçã" não está na lista!')
# #Ordene a lista em ordem alfabética.
# frutas.sort()#sort coloca a lista em orde alfabética e  altera a lista original, sorted retorna uma lista nova
# print(frutas)
# #Conte quantos elementos há na lista usando len().
# quantidade = len(frutas)
# print(f'A quantidad de frutas na lista {frutas} é um total de {quantidade} frutas.')
# #Inverta a ordem dos elementos da lista.
# # frutas.reverse()
# # print(frutas)
# #ou
# frutas_invertidas = frutas[::-1]
# print(frutas_invertidas)

#Crie uma nova lista que seja a junção de duas listas de frutas.
# frutas_1 = ['maçã', 'banana', 'goiaba']
# frutas_2 = ['pinha', 'melão', 'mamão']

# frutas_total = frutas_1 + frutas_2 #usar + para criar uma nova lista juntando os valores
# print(frutas_total)

#ou

# frutas_1 = ['maçã', 'banana', 'goiaba']
# frutas_2 = ['pinha', 'melão', 'mamão']

# frutas_1.extend(frutas_2)#usar o .extend para alterar a lista, adicionando os valores de outra lista existente
# print(frutas_1)

#EXERCÍCIO DE FIXAÇÃO PARA USO DE TUPLAS
#Crie uma tupla com 4 cores.
# cores = ('azul', 'vermelho', 'branco', 'roxo')
# #Acesse o último item da tupla usando índice negativo.
# print(cores[-1])
# #Verifique se a cor "azul" está na tupla.
# if 'azul' in cores:
#     print('A cor "azul" está na tupla.')
# else:
#     print('A cor "azul" não está na tupla.')
# #Converta a tupla em lista, adicione um novo item, e converta de volta para tupla.
# lista_nova = list(cores)
# lista_nova.append('amarelo')
# cores_nova = tuple(lista_nova)
# print(cores_nova)
#Crie uma tupla com apenas um elemento (e confirme que é uma tupla).
# tupla_um_elemento = ('azul',)#importante botar a vírgula para reconhecer como tupla
# print(tupla_um_elemento)
# print(type(tupla_um_elemento))

#Use len() para contar quantos itens há em uma tupla.
# cores = ('azul', 'vermelho', 'branco', 'roxo')

# qtd_cores = len(cores)
# print(f'A quantidade de cores na lista {cores} é um total de {qtd_cores} cores.')
# #Percorra a tupla com um laço for e exiba cada item.
# for cor in cores:
#     print(cor)
# #atualize a tupla em ordem alfabética
# cores_ordenadas = tuple(sorted(cores))
# print(cores_ordenadas)

#Peça ao usuário para digitar 5 números e armazene em uma lista. 
# Depois, exiba o maior e o menor número.
# numeros = []

# for i in range(5):
#     numero = int(input('Digite um número aleatório: '))
#     numeros.append(numero)

# print('Números digitados: ', numeros)
# print('O maior número digitado foi: ', max(numeros))
# print('O menor número digitado foi: ', min(numeros))

# numeros.sort()
# print(f'Os números {numeros} em ordem alfabética.')


#Crie uma tupla com os dias da semana e 
# permita que o usuário digite um número (0 a 6)
#  para exibir o dia correspondente.
#---------------------------------------------------------------------------------
# dias_semana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')

# numero = int(input('Escolha um número de 0 à 6: '))

# if 0 <= numero <= 6:
#     print(f'O dia correspondente da semana é: {dias_semana[numero]}')
# else:
#     print('Número inválido. Digite um número entre 0 e 6: ')
#----------------------------------------------------------------------------------

#EXERCÍCIO UDEMY LISTAS
"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""


# lista = []#criando uma lista vazia para ser incrementada pelo usuário

# while True:
#     print('Selecione uma opção: ')
#     opcao = input('[i] inserir\n[a] apagar\n[l] listar:\n[s] sair:\n ')#interação com usuário

#     if opcao == 'i':
#         item = input('Digite o nome do produto que deseja selecionar: ')
#         lista.append(item)#adicionando o item à lista vazia

#     elif opcao == 'a':
#         if lista:#conferindo se a lista não está vazia
#             for i, item in enumerate(lista):#para cada indice(i) e cada item dentro da lista enumerada, faça:
#                 print(f'[{i}] {item}')#exibe na tela o índice e nome do produto

#             indice = input('Digite o número do produto que deseja apagar da lista: ')

#             if indice.isdigit():#confere se o número digitado é positivo
#                 indice = int(indice)# transforma o número digitado em inteiro, por garantia

#                 if 0 <= indice < len(lista):#0 <= indice, garante que o indice não pode ser negativo
#                                         #< len lista, garante que o indice deve ser menor que o tamanho da lista
#                     lista.pop(indice)#retira da lista o índice selecionado pelo usuário
#                     print(f'Item {indice, item} removido com sucesso!')
#                 else:
#                     print('Item fora da faixa!')#índice não consta na lista
#             else:
#                 print('Digite um número válido!')#índice digitado não numérico
#         else:
#             print('Lista vazia!')#sem itens na lista

#     elif opcao == 'l':
#         if lista:#confere se a lista não está vazia
#             for i, item in enumerate(lista):#para cada índice e item em lista enumerada, faça:
#                 print(f'[{i}] {item}')
#         else:
#             print('Lista vazia.')
        
#     elif opcao == 's':
#         print('Fechando o programa!')
#         break#para o laço e a execução do programa!
#     else:
#         print('Opção inválida!')#mostra que a opção escolhida não existe

#-------------------------------------------------------------------------

lista1 = {
    'Nome':'Ari',
    'Idade':37,
    'Cidade':'Recife'
}
            
print(lista1)
lista1['País'] = 'Brasil' #adiciona uma chave e um valor ao dicionário
print(lista1)
lista1['Cidade'] = 'Olinda' #subcreve o valor da chave existente
print(lista1)

lista_tupla = tuple(lista1.items())
print(lista_tupla)

lista_lista = list(lista1.items())
print(lista_lista)

