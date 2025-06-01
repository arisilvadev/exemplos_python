
#prova do conteúdo ESTRUTURAS DE REPETIÇÃO
#LAÇO "FOR"
# [LPIA-A04] Você está desenvolvendo um programa em Python para calcular 
# a soma dos números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, 
# representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo
# e somar apenas os números pares. Implemente a estrutura 'else' para exibir 
# uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

soma_pares = 0
tem_par = False  

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        tem_par = True
else:
    if not tem_par:
        print("O intervalo não tem números pares!")

print(f"Soma dos números pares:{soma_pares}")
