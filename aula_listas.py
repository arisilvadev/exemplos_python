# 01 - Faça a definição de uma lista contendo os números de 1
# até 5. Finalmente, utilize o print() para exibir os valores
# da lista.

# numeros = [1,2,3,4,5]
# print(numeros)

# 02 - Faça a definição de uma lista contendo as vogais.
# Finalmente, utilize o print() para exibir os valores da lista.

# vogais = ['a','e','i','o','u']
# print(vogais)

# 03 - Defina uma lista com 5 itens que tenha, pelo menos, 3
# classes diferentes. Utilize o print() para exibir o
# terceiro elemento dessa lista.

# lista = [1, 'a', 2.0]
# print(lista[-1]) #ou índice 2(positivo)

# lista_itens = [
#     '2 fardos de arroz',
#     '2 fardos de feijão',
#     '1 fardo de leite em pó',
# ]
# lista_itens[0] = '2 sacos de farinha'

# print('Lista de compras', end='\n\n')
# for item in lista_itens:
#     print('[ ]', item)


#TUPLAS
# frutas = ('maçã', 'laranja', 'goiaba', 'uva', 'melão', 'uva')

# indice_uva = frutas.index('uva')#index mostra o índice do ítem dentro da tupla
# print('Índice da uva:', indice_uva)

# quantidade_uva = frutas.count('uva')#count mostra a quantidade de ocorrências do ítem da lista
# print('Quantidade uvas: ', quantidade_uva)

# 04 - Crie uma tupla para representar as informações de três
# palestrantes, cada uma contendo o nome, o tema da
# palestra e a instituição à qual estão vinculados.

# Exiba na tela as informações do terceiro palestrante,
# incluindo nome, tema da palestra e instituição.

# Definindo a tupla com informações dos palestrantes
# palestrantes = (
#     ("Ana Silva", "Inteligência Artificial", "Universidade A"),
#     ("Carlos Souza", "Cibersegurança", "Instituto B"),
#     ("Mariana Lima", "Computação Quântica", "Universidade C")
# )

# # Acessando e exibindo as informações do terceiro palestrante
# nome, tema, instituicao = palestrantes[2]

# print("Informações do terceiro palestrante:")
# print("Nome:", nome)
# print("Tema da palestra:", tema)
# print("Instituição:", instituicao)

#exemplo prático:

# pessoas = (
#     ('Ari silva', 'Python', 'Unibra'),
#     ('Maria Lago', 'Direito', 'Unibra'),
#     ('Chico Pug', 'Cachorros', 'Unicasa')
# )

# nome, tema, instituicao = pessoas[2]
# print('Informações do terceiro palestrante: ', end='\n\n')
# print('Nome do palestrante: ', nome, end='\n\n')
# print('Tema da palestra: ', tema, end='\n\n')
# print('Instituição de ensino: ', instituicao, end='\n\n')

# #EXEMPLO PRÁTICO 02
# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

# resultados = [
#     ("Equipe A", [8, 9, 10]),
#     ("Equipe B", [7, 6, 7]),
#     ("Equipe C", [10, 10, 9]),
#     ("Equipe D", [6, 5, 6])
# ]

# # Calcular médias e criar lista de classificação
# classificacao = [(equipe, sum(pontos)/len(pontos)) for equipe, pontos in resultados]

# # Ordenar em ordem decrescente
# classificacao.sort(key=lambda x: x[1], reverse=True)

# # Exibir classificação final
# print("Classificação Final:")
# for equipe, media in classificacao:
#     print(f"{equipe} - Média: {media:.2f}")

resultados = [
    ("Equipe A", [8, 9, 10]),
    ("Equipe B", [6, 7, 5]),
    ("Equipe C", [10, 10, 9])
]

classificacao = []  # lista vazia para armazenar (equipe, média)

for equipe, pontos in resultados:
    media = sum(pontos) / len(pontos)
    classificacao.append((equipe, media))  # adiciona a tupla na lista
    classificacao_ordenada = sorted(classificacao, key=lambda x: x[1], reverse=True)

# Ordena a lista pela média em ordem decrescente
classificacao.sort(key=lambda x: x[1], reverse=True)# key é um argumento que define com base em quê
#lambda é usado quando não se tem uma função pronta como 'len', 'sum', etc

# Exibe a classificação com for para ficar uma informação embaixo da outra
for equipe, media in classificacao:
    print(f'{equipe}: {media:.2f}')