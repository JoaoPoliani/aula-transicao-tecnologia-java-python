import Livro

livros = []

def cadastrarLivro(titulo, autor):
    if titulo.strip() == "" or autor.strip() == "":
        return "Título e autor não podem ser vazios."

    livros.append({
        "titulo": titulo, 
        "autor": autor,
        "emprestado": False
    })

    return f"Livro '{titulo}' cadastrado com sucesso."

def listarLivros():
    return list(livros)

def pesquisarPorTitulo(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
        
    return None

def emprestarLivro(titulo):
    livro = pesquisarPorTitulo(titulo)

    if livro is None:
        return "Livro não encontrado."
    
    return Livro.emprestar(livro)

def devolverLivro(titulo):
    livro = pesquisarPorTitulo(titulo)

    if livro is None:
        return "Livro não encontrado."
    
    return Livro.devolver(livro)
