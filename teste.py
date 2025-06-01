
# Solicite dois números e a operação desejada (+, -, *, /) e realize o cálculo.
import os
titulu = 'Calculadora 1.0'

while True:
    print(f'{titulu:=^40}')
    numero_1 = int(input('Digite o primeiro número para operação ou 0 para sair: '))
    if numero_1 == 0:
        print('Fechando a calculadora!')
        break
    numero_2 = int(input('Digite o segundo número para operação: '))
    operacao = input('Digite qual operação deseja fazer: [+], [-], [*], [/]: ')
    if operacao != '+-*/':
        print('Digite um operador válido!')
        continue

    
    if operacao == '+':
        print(f'O resultado de {numero_1} + {numero_2} é: {numero_1 + numero_2}')
    elif operacao == '-':
        print(f'O resultado de {numero_1} - {numero_2} é: {numero_1 - numero_2}')
    elif operacao == '*':
        print(f'O resultado de {numero_1} x {numero_2} é: {numero_1 * numero_2}')
    else:
        print(f'O resultado de {numero_1} / {numero_2} é: {numero_1 / numero_2:.0f}')
    input('Digite ENTER para continuar!')
    os.system('cls')


