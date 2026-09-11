class Disciplina: 

    def __init__(self, codigo, nome):
        if nome == "":
            raise ValueError("Nome do disciplina é obrigatorio")

        self.codigo = codigo
        self.nome = nome
    

    def __str__(self):
        return f"{self.codigo} - {self.nome}"