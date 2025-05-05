livros = []

def adicionar_Livro():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    while True:
        try:
            ano_input = input("Digite o ano do livro: ")
            if ano_input.isdigit() and len(ano_input) == 4:
                ano_publi = int(ano_input)
                break
            else:
                print("Digite 4 digitos.")
        except ValueError:
            print("Digite o ano corretamente.")     
    
    while True:
        try:
            isbn_input = input("Digite o ISBN do livro: ")
            if isbn_input.isdigit() and len(isbn_input) > 10 and len(isbn_input) <= 13:
                cod_isbn = int(isbn_input)
                break
            else:
                print("Preencha corretamente.")
        except ValueError:
            print("Digite o ISBN corretamente.")    
    
    
    livro = {
        "titulo":titulo,
        "autor":autor,
        "ano":ano_publi,
        "isbn":cod_isbn       
    }
    
    livros.append(livro)
    print("Livro adicionado com sucesso!")
    
    
def atualizar_Livros():
    if not livros:
        print("Nenhum livro na lista.")
        return
    
    for i, livro in enumerate(livros, start=1):
        print(f"\nLivro {i}")
        for chave, valor in livro.items():
            print(f"{chave.capitalize()} : {valor}")
    
    try:
        num_livro = int(input("Qual livro você deseja atualizar? "))
        indice_livro = num_livro - 1

        if 0 <= indice_livro < len(livros):
            livro = livros[indice_livro]

            # Atualizar título
            print(f"Título atual: {livro['titulo']}")
            if input("Deseja alterar o título? (S/N): ").lower() == "s":
                livro['titulo'] = input("Digite o novo título: ")
                print("Título atualizado com sucesso!")

            # Atualizar autor
            print(f"Autor atual: {livro['autor']}")
            if input("Deseja alterar o autor? (S/N): ").lower() == "s":
                livro['autor'] = input("Digite o novo nome do autor: ")
                print("Autor atualizado com sucesso!")

            # Atualizar ano
            print(f"Ano atual: {livro['ano']}")
            if input("Deseja alterar o ano? (S/N): ").lower() == "s":
                while True:
                    novo_ano = input("Digite o novo ano (4 dígitos): ")
                    if novo_ano.isdigit() and len(novo_ano) == 4:
                        livro['ano'] = int(novo_ano)
                        print("Ano atualizado com sucesso!")
                        break
                    else:
                        print("Ano inválido. Digite 4 dígitos.")

            # Atualizar ISBN
            print(f"ISBN atual: {livro['isbn']}")
            if input("Deseja alterar o ISBN? (S/N): ").lower() == "s":
                while True:
                    novo_isbn = input("Digite o novo ISBN (10 a 13 dígitos): ")
                    if novo_isbn.isdigit() and 10 <= len(novo_isbn) <= 13:
                        livro['isbn'] = int(novo_isbn)
                        print("ISBN atualizado com sucesso!")
                        break
                    else:
                        print("ISBN inválido. Digite entre 10 e 13 dígitos.")
        else:
            print("Número inválido. Escolha um livro da lista.")

    except ValueError:
        print("Entrada inválida. Digite apenas números.")

    
        
    
def listar_Livros():
    if not livros:
        print("Nenhum livro adicionado...")
    else:
        for i, livro in enumerate(livros, start=1):
            print(f"\nLivro {i}")
            for chave, valor in livro.items():
                print(f"{chave.capitalize()} : {valor}")
                
def deletar_Livro():
    try:
        if not livros:
            print("Nenhum livro na lista.")
        else:
            for i, livro in enumerate(livros, start=1):
                print(f"\n{i} - Livro: ")
                for chave, valor in livro.items():
                    print(f"{chave.capitalize()} : {valor}")
            valor = int(input("Qual livro você deseja deletar: "))
            indice = valor - 1
            if indice >= 0 and indice < len(livros):
                livro_escolhido = livros[indice]
                titulo = livro_escolhido.get("titulo", "Desconhecido")
                opcao_delete = input(f"\n Tem certeza que deseja excluir o livro \"{titulo}\" ? (S/N) : ")
                if opcao_delete.lower() == "s":
                    livros.pop(indice)
                    print("Livro deletado com sucesso!")
                else:
                    print("Operação cancelada.") 
            else:
                print("Número inválido. Digite um número da lista")
            
    except ValueError:
        print("Entrada inválida. Digite apenas números.")




while True:
    
    try:
        print("""
    ======= MENU ========      
    01 - Adicionar Livro
    02 - Listar Livros
    03 - Deletar Livro
    04 - Atualizar Livro
    05 - Sair 
            """)
        
        opcao = int(input("Escolha sua opção: "))
        
        if opcao == 1:
            adicionar_Livro()
        elif opcao == 2:
            listar_Livros()
        elif opcao == 3:
            deletar_Livro()
        elif opcao == 4:
            atualizar_Livros()
        elif opcao == 5:
            break
        else:
            print("Digite um número de 1 a 5.")
        
    except ValueError:
        print("Digite apenas números.")
    