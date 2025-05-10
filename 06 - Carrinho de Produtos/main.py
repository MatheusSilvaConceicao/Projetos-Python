# Dicionário com os itens disponíveis e seus respectivos preços
itens = {"caneta": 3.50, "lapis": 1.00, "borracha": 1.00}

# Lista que irá armazenar os itens adicionados ao carrinho
carrinho = []

# Função para adicionar itens ao carrinho
def adicionar_Item():
    i = 1
    # Exibe os itens disponíveis com numeração
    for item, valor in itens.items():
        print(f"{i} - {item} : R${valor:.2f}")
        i += 1

    # Solicita ao usuário o nome do item que deseja adicionar
    adicionar_item = input("Qual item você deseja adicionar ? ")

    # Verifica se o item está disponível
    if adicionar_item in itens.keys():
        # Adiciona o item ao carrinho com seu preço
        carrinho.append({adicionar_item: itens[adicionar_item]})
        print(f"{adicionar_item} foi adicionado ao carrinho.")
        print("Seu carrinho tem: ")
    else:
        print("Esse item não está disponível")

    # Exibe os itens do carrinho
    x = 1
    for produto in carrinho:
        for item, v_produto in produto.items():   
            print(f"{x} - {item} - R${v_produto:.2f}")  
            x += 1
    return

# Função para remover itens do carrinho
def remover_Item():
    if not carrinho:
        print("Seu carrinho está vazio :(")
    else:
        try:
            # Mostra os itens do carrinho com numeração
            i = 1
            for produto in carrinho:
                for item, v_produto in produto.items():
                    print(f"{i} - {item} - R${v_produto:.2f}")
                    i += 1
            # Solicita qual item o usuário deseja remover
            indice = int(input("Digite o número do item a remover: ")) - 1
            if 0 <= indice < len(carrinho):
                removido = carrinho.pop(indice)
                print(f"Item removido: {list(removido.keys())[0]}")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Digite um número válido.")

# Função para visualizar os itens no carrinho e o valor total
def ver_Carrinho():
    if carrinho:
        i = 1
        total = 0
        # Percorre todos os produtos no carrinho
        for produto in carrinho:
            for chave, v_produto in produto.items():
                print(f'{i} - {chave} : R${v_produto:.2f}')
                total += v_produto
                i += 1
        print(f"VALOR TOTAL: R${total:.2f}")     
    else:
        print("Você ainda não possui produtos no carrinho.")

# Menu principal do sistema
print("""
======== MENU ========
01 - Adicionar
02 - Remover
03 - Ver total
04 - Finalizar
05 - Sair
======================
""")

# Loop principal que executa o menu até o usuário sair
while True:
    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionar_Item()
        elif opcao == 2:
            remover_Item()
        elif opcao == 3:
            ver_Carrinho()
        elif opcao == 4:
            print("Compra finalizada! Obrigado pela preferência.")
        elif opcao == 5:
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Digite um número entre 1 e 5")

    except ValueError:
        print("Digite apenas números")
