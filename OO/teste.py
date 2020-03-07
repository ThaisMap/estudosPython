def cria_conta (numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor
    return conta

def sacar(conta, valor):
    conta["saldo"] -= valor
    return conta

def extrato(conta):
    print (conta["saldo"])