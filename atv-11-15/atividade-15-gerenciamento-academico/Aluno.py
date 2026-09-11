class Aluno:

    def __init__(self, matricula, nome):
        if nome == "":
            raise ValueError("Nome do aluno é obrigatorio")

        self.matricula = matricula
        self.nome = nome

    def __str__(self):
        return f"{self.matricula} - {self.nome}"