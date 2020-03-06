import random


def jogar():
    imprime_mensagem_abertura()
   
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False

    erros = 0
    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = receber_chute()

        if chute not in palavra_secreta:
            erros += 1
        else:
           letras_acertadas = preenche_letras_acertadas(chute, palavra_secreta, letras_acertadas)

        print(letras_acertadas)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 6

    imprime_mensagem_final(acertou)


def imprime_mensagem_abertura():
    print("*******************************")
    print("* Bem vindo ao jogo de Forca! *")
    print("*******************************")


def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))]

    palavra_secreta = palavra_secreta.upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    return letras_acertadas
    

def receber_chute():
    chute = input("Qual a letra? ")
    return chute.strip().upper()


def preenche_letras_acertadas(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1
    return letras_acertadas


def imprime_mensagem_final(acertou):
    if acertou:
        print("Você ganhou!")
    else:
        print("Você enforcou")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
