livro = {
    "titulo": "",
    "autor": "",
    "emprestado": False
}

def emprestar(livro):
    if not livro["emprestado"]:
        livro["emprestado"] = True
        return f"Livro '{livro['titulo']}' emprestado com sucesso."
        
    else:
        return f"Livro '{livro['titulo']}' já está emprestado."

def devolver(livro):
    if livro["emprestado"]:
        livro["emprestado"] = False
        return f"Livro '{livro['titulo']}' devolvido com sucesso."
    else:
        return f"Livro '{livro['titulo']}' não está emprestado."

