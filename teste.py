
def soma(a,b):
    return a+b 

def subtração(a,b):
    return a-b 

def multiplicação(a,b):
    return a*b

def divisão(a,b):
    if b == 0:
        return 'Erro! Divisão não pode ser por 0!'
    return a/b
    
def menu():
    print('\n==Calculadora 2.0==')
    print('[1] Soma.')
    print('[2] Subtração.')
    print('[3] Multiplicação.')
    print('[4] Divisão.')
    print('[5] Sair.')
    
while True:
    menu()
    opcao = input('Escolha uma operação: ')
    
    if opcao == 5:
        print('Fechando calculadora!')
        break
    elif opcao in ['1','2','3','4']:
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
        except ValueError:
            print('Erro! Digite apenas números!')
            continue
        if opcao == '1':
            print(f'Resultado = {soma(num1, num2)}')
        elif opcao == '2':
            print(f'Resultado = {subtração(num1, num2)}')
        elif opcao == '3':
            print(f'Resultado = {multiplicação(num1, num2)}')
        elif opcao == '4':
            print(f'Resultado = {divisão(num1, num2)}')
    else:
        print('Erro! Digite um número entre 1 e 5!')
    
    
    
        


