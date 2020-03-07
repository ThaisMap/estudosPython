class Conta:
    def __init__(self, numero, titular, saldo):
        print("Construindo conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor
        print("{} depositado".format(valor))

    def sacar(self, valor):
        self.saldo -= valor
        print("{} sacado".format(valor))