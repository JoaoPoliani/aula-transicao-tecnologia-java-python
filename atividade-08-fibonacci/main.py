qtd = int(input("Digite a quantidade de termos da sequencia de Fibonacci: "))

if qtd <= 0:
    print("A quantidade deve ser maior que zero")
    exit()

anterior = 0
atual = 1

for i in range(1, qtd + 1):
    print(anterior, end=" ")

    proximo = anterior + atual
    anterior = atual
    atual = proximo

print()