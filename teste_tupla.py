# nomes = [
#     ('ari silva', 38),
#     ('maria lago', 43),
#     ('chico pug', 5)
# ]

# ordenado = sorted(nomes, key=lambda x: x[1])
# for item in ordenado:
#     print(item)
#------------------------------------------
# def calcular_media(lista):
#     return sum(lista) / len(lista)

# notas = [7, 8, 9]
# media = calcular_media(notas)
# print(f"Média: {media:.2f}")
#------------------------------------------
nomes = ["joão", "maria", "ana", "Carlos"]

# Ordenar com base no tamanho do nome
nomes_ordenados = sorted(nomes, key=len)
print(nomes_ordenados)