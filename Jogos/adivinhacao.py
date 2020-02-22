print("**************************************")
print("* Bem vindo ao jogo de adivinhação!! *")
print("**************************************")

numero_secreto = 42

chute = int(input("Digite o número secreto: "))

print("Você digitou ", chute)

if chute == numero_secreto:
    print("Você acertou!")
else:
    print("Você errou")