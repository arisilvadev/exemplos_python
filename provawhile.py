# [LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. 
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número.

# Implemente o jogo utilizando um loop while para permitir que o jogador faça 
# múltiplas tentativas até acertar ou atingir o limite de tentativas. 
# Utilize a estrutura else para exibir uma mensagem de encorajamento 
# caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

import random
numero_adivinhe = random.randint(1,10)
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
    tentativas += 1

    if palpite == numero_adivinhe:
        print(f'Parabéns! Você acertou o número! O número secreto é {numero_adivinhe}')
        break
else:
    print("Que pena! Suas tentativas acabaram. O número era", numero_adivinhe)