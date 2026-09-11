qtdAlunos = 5

nomes = [None] * qtdAlunos
notas = [None] * qtdAlunos

def cadastrarAlunos():
    for i in range(qtdAlunos):
        nomes[i] = input(f"Digite o nome do {i + 1}º aluno: ")
        notas[i] = float(input(f"Digite a nota do {i + 1}º aluno: "))

def exibirAlunos():
    print("Alunos cadastrados:")

    for i in range(qtdAlunos):
        print(f"Nome: {nomes[i]}, Nota: {notas[i]}")

def calcularMedia():
    soma = sum(notas)

    media = soma / qtdAlunos
    
    return media

def exibirAlunoComMaiorNota():
    maiorNota = max(notas)
    indiceMaior = notas.index(maiorNota)
    print(f"Aluno com a maior nota: {nomes[indiceMaior]}, Nota: {maiorNota}")