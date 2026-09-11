from SistemaAcademico import SistemaAcademico

def exibirMenu():
    print()
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar disciplina")
    print("3 - Matricular aluno")
    print("4 - Lançar nota")
    print("5 - Consultar boletim")
    print("6 - Listar alunos")
    print("7 - Listar disciplinas")
    print("0 - Sair")
    print("Escolha uma opção: ")


def executarOpcao(sistema, opcao):

    match opcao:
        case 1:
            cadastrarAluno(sistema)

        case 2:
            cadastrarDisciplina(sistema)

        case 3:
            matricularAluno(sistema)

        case 4:
            lancarNota(sistema)

        case 5:
            consultarBoletim(sistema)

        case 6:
            listarAlunos(sistema)

        case 7:
            listarDisciplinas(sistema)

        case 0:
            print("Encerrando...")

        case _:
            print("Opção inválida.")


def cadastrarAluno(sistema):
    matricula = int(input("Matrícula do aluno: "))
    nome = input("Nome do aluno: ")

    sistema.cadastrarAluno(matricula, nome)

    print("Aluno cadastrado.")


def cadastrarDisciplina(sistema):
    codigo = int(input("Código da disciplina: "))
    nome = input("Nome da disciplina: ")

    sistema.cadastrarDisciplina(codigo, nome)

    print("Disciplina cadastrada.")


def matricularAluno(sistema):
    matriculaAluno = int(input("Matrícula do aluno: "))
    codigoDisciplina = int(input("Código da disciplina: "))

    sistema.matricularAluno(matriculaAluno, codigoDisciplina)

    print("Matrícula realizada.")


def lancarNota(sistema):
    matriculaAluno = int(input("Matrícula do aluno: "))
    codigoDisciplina = int(input("Código da disciplina: "))
    nota = float(input("Nota: "))

    sistema.lancarNota(matriculaAluno, codigoDisciplina, nota)

    print("Nota lançada.")


def consultarBoletim(sistema):
    matriculaAluno = int(input("Matrícula do aluno: "))

    boletim = sistema.consultarBoletim(matriculaAluno)

    if len(boletim) == 0:
        print("Aluno sem disciplinas matriculadas.")
        return

    for matricula in boletim:
        situacao = "Aprovado" if matricula.aprovado() else "Reprovado"

        print(
            f"{matricula.disciplina.nome} - "
            f"Média: {matricula.calcularMedia():.2f} - "
            f"{situacao}"
        )


def listarAlunos(sistema):
    alunos = sistema.listarAlunos()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(aluno)


def listarDisciplinas(sistema):
    disciplinas = sistema.listarDisciplinas()

    if len(disciplinas) == 0:
        print("Nenhuma disciplina cadastrada.")
        return

    for disciplina in disciplinas:
        print(disciplina)


sistema = SistemaAcademico()

opcao = -1

while opcao != 0:

    exibirMenu()

    try:
        opcao = int(input())

        executarOpcao(sistema, opcao)

    except ValueError as erro:
        print(erro)