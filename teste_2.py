variavel = input('Digite o seu nome: ')
nome_contrario = variavel[: : -1]
print(nome_contrario)
letra_final = variavel[-1]
print(f'A letra final do seu nome é:' , letra_final)
letra_inicial = variavel[0]
print(f'A letra inicial do seu nome é: ', letra_inicial)
print(f'Seu nome tem ' , len(variavel), 'carateres.')