import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)  # Gera número Secreto aleatório entre 1 e 100
total_tentativas = 0  # escolhe a quantidade de tentativas

print("Qual o nível de dificuldade?")  # escolhe a dificuldade do jogo
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if nivel == 1:
    total_tentativas = 20
elif nivel == 2:
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):  # Contador de tentativas
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Voce digitou", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:  # Verificar números entre 1 e 100
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:  # Mensagem de acerto
        print("Você acertou!")
        break
    else:  # Mensagem de erro + dica caso a tentativa seja menor ou maior que o número secreto
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo")
