num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = int(input("Digite o terceiro numero inteiro: "))

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print(f"Maior numero: {maior}")