# escrever um código com tudo o que se aprendeu até aqui!
#estruturas de decisão
# Faça um Programa que peça dois números e imprima o maior deles.

# num_1 = input('Digite o número 1: ')

# num_2 = input('Digite o número 2: ')

# if num_1 > num_2:
#     print('O número 1 é maior que o número 2!')
# else:
#     print('O número 2 é maior que o número 1!')

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
produto_1 = float(input('Digite o valor do produto 1: '))
produto_2 = float(input('Digite o valor do produto 2: '))
produto_3 = float(input('Digite o valor do produto 3: '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print('O produto 1 está mais barato. Você deve comprá-lo!')
elif produto_2 < produto_1 and  produto_2 < produto_3:
    print('O produto 2 está mais barato. Você deve comprá-lo!')
else:
   print('O produto 3 está mais barato. Você deve comprá-lo!')
