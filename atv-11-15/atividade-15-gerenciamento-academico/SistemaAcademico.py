from Aluno import Aluno
from Disciplina import Disciplina
from Matricula import Matricula

class SistemaAcademico:

    def __init__(self):
        self.alunos = []
        self.disciplinas = []
        self.matriculas = []

    def cadastrarAluno(self, matricula, nome):
        if self.buscarAluno(matricula):
            raise ValueError("Já existe aluno com essa matrícula.")

        self.alunos.append(Aluno(matricula, nome))

    def cadastrarDisciplina(self, codigo, nome):
        if self.buscarDisciplina(codigo):
            raise ValueError("Já existe disciplina com esse código.")

        self.disciplinas.append(Disciplina(codigo, nome))

    def matricularAluno(self, matriculaAluno, codigoDisciplina):
        aluno = self.buscarAluno(matriculaAluno)
        disciplina = self.buscarDisciplina(codigoDisciplina)

        if not aluno:
            raise ValueError("Aluno não encontrado.")

        if not disciplina:
            raise ValueError("Disciplina não encontrada.")

        if self.buscarMatricula(matriculaAluno, codigoDisciplina):
            raise ValueError("Aluno já matriculado nessa disciplina.")

        self.matriculas.append(Matricula(aluno, disciplina))

    def lancarNota(self, matriculaAluno, codigoDisciplina, nota):
        matricula = self.buscarMatricula(matriculaAluno, codigoDisciplina)

        if not matricula:
            raise ValueError("Matrícula não encontrada.")

        matricula.adicionarNota(nota)

    def listarAlunos(self):
        return self.alunos

    def listarDisciplinas(self):
        return self.disciplinas

    def consultarBoletim(self, matriculaAluno):
        if not self.buscarAluno(matriculaAluno):
            raise ValueError("Aluno não encontrado.")

        boletim = []

        for matricula in self.matriculas:
            if matricula.aluno.matricula == matriculaAluno:
                boletim.append(matricula)

        return boletim

    def buscarAluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno

        return None

    def buscarDisciplina(self, codigo):
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo:
                return disciplina

        return None

    def buscarMatricula(self, matriculaAluno, codigoDisciplina):
        for matricula in self.matriculas:
            if (matricula.aluno.matricula == matriculaAluno
                    and matricula.disciplina.codigo == codigoDisciplina):
                return matricula

        return None