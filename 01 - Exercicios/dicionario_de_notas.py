"""
Dicionário de Notas: Peça ao usuário para inserir o nome de um aluno e sua nota, armazenando os dados em um dicionário. Permita que o usuário insira quantos alunos quiser até digitar "sair".

"""
dados_aluno = {}

def tabela_menu():
    while True:
        print("1 - Adicionar Aluno e Nota")
        print("2 - Mostrar lista")
        print("0 - Sair")
        
        try:
            opcao_usuario = int(input("Escolha sua opção: "))
        except ValueError:
            print("Por favor, digite um número válido (0,1 ou 2).")
            continue
        
        match opcao_usuario:
            case 1:
                adicionar_aluno()
            case 2: 
                mostrar_aluno()
            case 0:
                print("Até logo")
                break
            case _:
                print("Digite apenas 1,2 ou 0: ")
        
       
    
def adicionar_aluno():
    while True:
        nome_aluno = input("Digite o nome do aluno (ou 'sair' para voltar ao menu): ")
        if nome_aluno.lower() == "sair":
            break
        try:
            nota_aluno = float(input(f"Digite a nota de {nome_aluno} : "))
            if nota_aluno >10 or nota_aluno < 0:
                print("A nota deve ser entre 0 e 10")
                continue
        except ValueError:
            print("Por favor, digite um valor número válido para nota.")
            continue
        dados_aluno[nome_aluno] = nota_aluno
        print(f"Aluno {nome_aluno} com nota {nota_aluno} foi adicionado com sucesso!")
    
def mostrar_aluno():
    if not dados_aluno:
        print("Nenhum aluno cadastrado no momento.")
    else:
        print("Lista de Alunos e Notas: ")
        for aluno, nota in dados_aluno.items():
            print(f"{aluno}: {nota}")
    
    
tabela_menu()