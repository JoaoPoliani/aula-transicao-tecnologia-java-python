numeros = [None] * 10
soma = 0

for i in range(0, 10):
    numeros[i] = int(input(f"Digite o {i + 1}º número: "))
    soma += numeros[i]

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

media = soma / len(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos números: {media}") 