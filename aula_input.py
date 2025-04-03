nome = str(input("Digite o nome do aluno: "))
nota_1 = float(input("Digite a nota 1 do aluno " + nome + ": "))
nota_2 = float(input("Digite a nota 2 do aluno " + nome + ": "))
nota_3 = float(input("Digite a nota 3 do aluno " + nome + ": "))
media = (nota_1 + nota_2 + nota_3) / 3
fim = ('Fim do programa')


if(media >=7):
    linha_1 = f'Parabéns! Você foi "aprovado" e sua média é: {media:.2f}'
    print(linha_1)
elif(media >=5):
    linha_2 = f'Você está de "recuperação" e sua média é: {media:.2f}'
    print(linha_2)
    print("Você precisa estudar mais!")
elif(media <5):
    linha_3 = f'Você está "reprovado" e sua média é: {media:.2f}'
    print(linha_3)
    print("Você terá uma outra oportunidade no ano seguinte")
else:
    print("Digite um valor válido")

print(f'{fim:-^40}')
print(40 * '-')