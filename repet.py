import os


while True:#enquanto essa condição for verdadeira, então faça:
        nome_do_aluno = input('Digite o nome do aluno ou "sair" para fechar o programa: ')
        if nome_do_aluno == 'Sair' or nome_do_aluno == 'sair' or nome_do_aluno == 'SAIR':
            sair = ('Programa finalizado!')
            print(50 * '-')#vai retornar na tela 50 vezes o traço
            print(f'{sair:-^50}')
            break#comando break para a repetição while
        nota_1 = float(input(f'Digite a nota 1 do aluno {nome_do_aluno}: '))
        nota_2 = float(input(f'Digite a nota 2 do aluno {nome_do_aluno}: '))
        nota_3 = float(input(f'Digite a nota 3 do aluno {nome_do_aluno}: '))
        media = (nota_1+nota_2+nota_3) / 3
        
        if media >= 7:
              print(f'O aluno {nome_do_aluno} foi "APROVADO" e sua média foi {media:.2f}!\n{'-'*10}Parabéns!')
              input('Tecle enter para continuar!')
              os.system('cls')
        elif media >= 5:
              print(f'O aluno {nome_do_aluno} está de "RECUPERAÇÃO" e sua média foi {media:.2f}!')
              input('Tecle enter para continuar!')
              os.system('cls')
        elif media < 5:
              print(f'O aluno {nome_do_aluno} foi "REPROVADO" e sua média foi {media:.2f}!')
              input('Tecle enter para continuar!')
              os.system('cls')


    
  
    
    
    
    




       
