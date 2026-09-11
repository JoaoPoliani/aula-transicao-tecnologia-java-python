def exibir_menu():
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = int(input("Escolha uma opção: "))

    if opcao < 1 or opcao > 4:
        print("Opção inválida. Tente novamente.")
        return exibir_menu()
    
    return opcao

def calcular(opcao, num1, num2):
    match opcao:
        case 1:
            print(f"A soma de {num1} e {num2} é: {num1 + num2}")
            exit()
        case 2:
            print(f"A subtração de {num1} e {num2} é: {num1 - num2}")
            exit() 
        case 3:
            print(f"A multiplicação de {num1} e {num2} é: {num1 * num2}")  
            exit()
        case 4:
            if num2 != 0:
                print(f"A divisão de {num1} e {num2} é: {num1 / num2}")
                exit()
            else:
                print("Erro: Divisão por zero não é permitida.")
                exit()

opcao = exibir_menu()

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

calcular(opcao, num1, num2)