
# Desenvolva um programa em Python para calcular a média de notas 
# de alunos em uma disciplina. O programa deve solicitar ao usuário
#  o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. 
#  Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada 
# aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

qtd_alunos = int(input("Digite a quantidade de alunos: "))
soma_medias = 0

for i in range(qtd_alunos):
    nome = input(f"\nNome do aluno {i+1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    status = "Aprovado" if media >= 7 else "Reprovado"

    print(f"{nome} - Notas: {nota1}, {nota2}, {nota3} | Média: {media:.2f} | {status}")

media_geral = soma_medias / qtd_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")