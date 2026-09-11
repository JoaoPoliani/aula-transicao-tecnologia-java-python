numero = int(input("Digite um numero inteiro positivo: "))

if numero < 0:
    print("O numero deve ser positivo")
    exit()

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"Fatorial: {fatorial}")    