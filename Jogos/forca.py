def jogar():
    print("*******************************")
    print("* Bem vindo ao jogo de Forca! *")
    print("*******************************")

    palavra_secreta = "cachorro"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra na posicao {}".format(index))
            index = index+1
        print("Jogando...")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
