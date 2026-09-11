class Matricula:

    def __init__(self, aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.notas = []

    def adicionarNota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10")

        self.notas.append(nota)

    def calcularMedia(self):
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        return self.calcularMedia() >= 7

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}"