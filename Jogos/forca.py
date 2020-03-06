import random
def jogar():
    print("*******************************")
    print("* Bem vindo ao jogo de Forca! *")
    print("*******************************")

    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))]

    palavra_secreta = palavra_secreta.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False

    erros = 0
    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        if chute not in palavra_secreta:
            erros += 1
        else:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index+1

        print(letras_acertadas)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 6

    print("Fim do jogo")
    if acertou:
        print("Você ganhou!")
    else:
        print("Você enforcou")


if __name__ == "__main__":
    jogar()
