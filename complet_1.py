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
   
salario_anterior = float(input("Digite seu salário atual: "))
salario_atual = 0.0
diferenca_entre_salarios = 0.0
percentual_de_aumento = 0.0

if salario_anterior <= 280:
    percentual_de_aumento = 20
elif salario_anterior <= 750:
    percentual_de_aumento = 15
elif salario_anterior <= 1500:
    percentual_de_aumento = 10
else:
    percentual_de_aumento = 5

diferenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
salario_atual = salario_anterior + diferenca_entre_salarios
print(f"Seu salário antes do reajuste era de R${salario_anterior:.2f}")
print(f"Seu salário foi aumentado em {percentual_de_aumento}%")
print(f"Seu salário foi aumentado em R${diferenca_entre_salarios:.2f}")
print(f"Seu salário atual é de R${salario_atual:.2f}")


   
   
