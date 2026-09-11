
numero = int
titular = str
saldo = float

def contaBancaria(numero, titular, saldoInicial):
    if saldoInicial < 0:
        raise ValueError("O saldo inicial não pode ser negativo")

    return {
        "numero": numero,
        "titular": titular,
        "saldo": saldoInicial
    }

def depositar(conta, valor):
    if valor <= 0:
        raise ValueError("O valor do depósito deve ser positivo")
    conta["saldo"] += valor

def sacar(conta, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo")
    if valor > conta["saldo"]:
        raise ValueError("Saldo insuficiente para o saque")
    conta["saldo"] -= valor


