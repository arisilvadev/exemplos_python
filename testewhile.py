
import random

# O programa escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
palpite = None

print("🎯 Jogo de Adivinhação 🎯")
print("Tente adivinhar o número que estou pensando (entre 1 e 100).")

while palpite != numero_secreto:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("🔻 Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("🔺 Muito alto! Tente um número menor.")
        else:
            print(f"✅ Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
    except ValueError:
        print("❗ Por favor, digite um número válido.")