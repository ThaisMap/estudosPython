class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __str__(self):
        return f"{self.nome} (self.{ano}) - {self.likes} likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    def __str__(self):
        return f"{self.nome} ({self.ano}) - {self.__duracao} minutos - {self.likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} ({self.ano}) - {self.temporadas} temporadas - {self.likes} likes"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._pogramas = programas

    @property
    def listagem(self):
        return self._pogramas

    def tamanho(self):
        return len(self._pogramas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

listinha = [atlanta, vingadores]
minha_play = Playlist("minha", listinha)

for programa in minha_play.listagem:
    print(programa)
