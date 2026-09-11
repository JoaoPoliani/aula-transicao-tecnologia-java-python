senha = input("Digite a senha: ")

tamanhoValido = len(senha) >= 8
possuiMaiuscula = False
possuiNumero = False

for char in senha:
    if char.isupper():
        possuiMaiuscula = True

    if char.isdigit():
        possuiNumero = True

if tamanhoValido and possuiMaiuscula and possuiNumero:
    print("Senha válida!")
else:
    print("Senha inválida!")