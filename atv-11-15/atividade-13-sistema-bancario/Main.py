import ContaBancaria

numero = input("Digite o número da conta: ")
titular = input("Digite o nome do titular: ")
saldoInicial = float(input("Digite o saldo inicial: "))

conta = ContaBancaria.contaBancaria(numero, titular, saldoInicial)

def exibirMenu():
    print("\n=== Menu ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir saldo")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))
    return opcao

def executarOpcao(conta, opcao):

    match opcao:

        case 1:
            valor = float(input("Valor do deposito: "))
            ContaBancaria.depositar(conta, valor)
            print("Deposito realizado")

        case 2:
            valor = float(input("Valor do saque: "))
            ContaBancaria.sacar(conta, valor)
            print("Deposito realizado")

        case 3:
            print(f"Saldo Atual: R$ {conta["saldo"]}")

        case 0:
            print("Encerrando...")

        case _:
            print("Opção invalida")

while True:

    opcao = exibirMenu()

    executarOpcao(conta, opcao)

    if opcao == 0:
        break

