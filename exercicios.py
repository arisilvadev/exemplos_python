# numero_1 = int(input('Digite qualquer número:'))
# numero_2 = int(input('Digite outro número:'))
# print(f'A soma dos dois números digitados é igual à: {numero_1 + numero_2}')
# print(40 * '-')

#exercicio 005 Faça um Programa que converta metros para centímetros.

# metros = float(input('Digite quantos metros serão convertidos: '))
# conversao = metros * 100
# print(f'A conversão de {metros} em centímetros é igual à: {conversao} centímetros')

#exercicio 008 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

# valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
# quant_horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))
# valor_salario = valor_hora * quant_horas
# print(f'O salário recebido no mês tem valor de: R$ {valor_salario:,.0f} ')

# #fatiamento de strings
# variavel = (len('Olá mundo!'))
# print(variavel[0:10:1])
# #[inicio:fim:passo]
#len: conta os caracteres


# """"""
# Exercício
#  Peça ao usuário para digitar seu nome
#  Peça ao usuário para digitar sua idade
#  Se nome e idade forem digitados:
#      Exiba:
#          Seu nome é {nome}
#          Seu nome invertido é {nome invertido}
#          Seu nome contém (ou não) espaços
#          Seu nome tem {n} letras
#          A primeira letra do seu nome é {letra}
#          A última letra do seu nome é {letra}
#  Se nada for digitado em nome ou idade: 
#      exiba "Desculpe, você deixou campos vazios."
#  """

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')


if nome != " " and idade != " ":
    print(f'Seu nome é: {nome}.')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if " " in nome:
        print('Seu nome contém espaços!')
    else:
        print('Seu nome não contém espaços!')

    print(f'Seu nome tem ', len(nome), "letras.")
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe! Você deixou campos em branco.')