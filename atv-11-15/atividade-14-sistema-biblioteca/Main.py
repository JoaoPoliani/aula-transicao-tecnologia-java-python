import Biblioteca


def exibirMenu():
    print("\n=== Sistema de Biblioteca ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Pesquisar livro por título")
    print("4. Emprestar livro")
    print("5. Devolver livro")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    return opcao


def executarOpcao(opcao):
    match opcao:
        case "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")

            resultado = Biblioteca.cadastrarLivro(titulo, autor)
            print(resultado)

        case "2":
            livros = Biblioteca.listarLivros()

            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                for livro in livros:
                    status = "Emprestado" if livro["emprestado"] else "Disponível"
                    print(
                        f"- {livro["titulo"]} por {livro["autor"]} "
                        f"({status})"
                    )

        case "3":
            titulo = input("Digite o título do livro: ")
            livro = Biblioteca.pesquisarPorTitulo(titulo)

            if livro:
                status = "Emprestado" if livro["emprestado"] else "Disponível"
                print(
                    f"- {livro["titulo"]} por {livro["autor"]} "
                    f"({status})"
                )
            else:
                print("Livro não encontrado.")

        case "4":
            titulo = input("Digite o título do livro: ")
            resultado = Biblioteca.emprestarLivro(titulo)
            print(resultado)

        case "5":
            titulo = input("Digite o título do livro: ")
            resultado = Biblioteca.devolverLivro(titulo)
            print(resultado)

        case "0":
            print("Saindo...")

        case _:
            print("Opção inválida.")


while True:
    opcao = exibirMenu()
    executarOpcao(opcao)

    if opcao == "0":
        break
