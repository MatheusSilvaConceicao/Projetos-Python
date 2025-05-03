itens = {"caneta": 3.50, "lapis": 1.00, "borracha": 1.00}
carrinho =[]


def adicionar_Item():
    i = 1
    for item, valor in itens.items():
        print(f"{i} - {item} : R${valor:.2f}")
        i += 1
    adicionar_item = input("Qual item você deseja adicionar ? ")
    if adicionar_item in itens.keys():
        carrinho.append({adicionar_item: itens[adicionar_item]})
        print(f"{adicionar_item} foi adicionado ao carrinho.")
        print("Seu carrinho tem: ")
    else:
        print("Esse item não está disponivel")
    x = 1
    for produto in carrinho:
        for item, v_produto in produto.items():   
            print(f"{x} - {item} - R${v_produto:.2f}")  
            x += 1
    return  
    
def remover_Item():
    if not carrinho:
        print("Seu carrinho está vazio :(")
    else:
        try:
            i = 1
            for produto in carrinho:
                for item, v_produto in produto.items():
                    print(f"{i} - {item} - R${v_produto:.2f}")
                    i += 1
            indice = int(input("Digite o número do item a remover: ")) - 1
            if 0 <= indice < len(carrinho):
                removido = carrinho.pop(indice)
                print(f"Item removido: {list(removido.keys())[0]}")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Digite um número válido.")
            

def ver_Carrinho():
    if carrinho:
        i = 1
        total = 0
        for produto in carrinho:
            for chave, v_produto in produto.items():
                print(f'{i} - {chave} : R${v_produto:.2f}')
                total += v_produto
                i += 1
        print(f"VALOR TOTAL: R${total:.2f}")     
    else:
        print("Você ainda não possui produtos no carrinho.")
    
print("""
======== MENU ========
01 - Adicionar
02 - Remover
03 - Ver total
04 - Finalizar
05 - Sair
======================
      """)
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
            print(opcao)
        elif opcao == 5:
            break
        else:
            print("Digite um número entre 1 e 5")

    except ValueError:
        print("Digite apenas números")