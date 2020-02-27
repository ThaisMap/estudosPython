
import forca
import adivinhacao

print("********************")
print("* Escolha seu jogo *")
print("********************")

escolhido = input("1 - Forca / 2 - Adivinhação")
if escolhido == "1":
    forca.jogar()
elif escolhido == '2':
    adivinhacao.jogar()
