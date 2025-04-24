# Inicializa uma lista vazia para armazenar as tarefas
lista = []

# Função para adicionar uma tarefa à lista
def adicionar_tarefa(lista):
    print("===== ADICIONAR TAREFA =====")
    # Solicita ao usuário que insira a descrição da tarefa
    tarefa = input("Qual é a tarefa? ").strip()
    # Verifica se a entrada não está vazia
    if tarefa:
        # Adiciona a tarefa à lista
        lista.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    else:
        # Informa ao usuário que a entrada é inválida
        print("Tarefa inválida! Não pode estar vazia.")

# Função para remover uma tarefa da lista
def remover_tarefa(lista):
    print("======= REMOVER TAREFA =======")
    # Lista as tarefas atuais
    listar_tarefa(lista)
    # Verifica se a lista está vazia
    if not lista:
        return
    
    try:
        # Solicita ao usuário que insira o número da tarefa a ser removida
        n = int(input("Escolha o número da tarefa que você deseja remover: "))
        # Verifica se o número está dentro do intervalo válido
        if 1 <= n <= len(lista):
            # Remove a tarefa correspondente
            removida = lista.pop(n - 1)
            print(f"Tarefa '{removida}' removida com sucesso!")
        else:
            # Informa ao usuário que o número é inválido
            print("Número da tarefa inválido.")
    except ValueError:
        # Informa ao usuário que a entrada não é um número válido
        print("Digite um número válido.")

def listar_tarefa(lista):
    print("======= TAREFAS =======")
    # Verifica se há tarefas na lista
    if lista:
        # Itera sobre a lista e imprime cada tarefa com seu número
        for i, tarefa in enumerate(lista, start=1):
            print(f"Tarefa {i}: {tarefa}")
    else:
        # Informa ao usuário que não há tarefas
        print("Nenhuma tarefa encontrada.")

# Loop principal do programa
while True:
    # Exibe o menu de opções
    print('''
======= To-Do List =======
01 - Adicionar tarefa
02 - Remover tarefa 
03 - Listar tarefas
04 - Sair 
==========================
''')

    try:
        # Solicita ao usuário que escolha uma opção
        opcao = int(input("Escolha sua opção: "))
    except ValueError:
        # Informa ao usuário que a entrada não é um número válido
        print("Digite um número válido.")
        continue  # Retorna ao início do loop

    # Verifica qual opção foi escolhida e chama a função correspondente
    if opcao == 1:
        adicionar_tarefa(lista)
    elif opcao == 2:
        remover_tarefa(lista)
    elif opcao == 3:
        listar_tarefa(lista)
    elif opcao == 4:
        # Encerra o loop e, consequentemente, o programa
        print("Saindo do programa...")
        break
    else:
        # Informa ao usuário que a opção é inválida
        print("Digite um valor correto.")
