from registro import despesas



def atualizar_gasto():
    if not despesas:
        print("Você não possui gastos.")
    else:
        for i, gasto in enumerate(despesas, start= 1):
            print(f"[{i}] {gasto['descricao']} - R${gasto['valor']:.2f}")
        
        num_gasto = int(input("Qual gasto você deseja atualizar ?"))
        ind_gasto = num_gasto - 1
        
        if 0 <= ind_gasto <= len(despesas):
            
            
            print(f"Descrição atual: {ind_gasto['descricao']}")
            if input("Você deseja alterar a descrição ? (S/N)").lower() == "s":
                gasto['descricao'] = input("Digite a nova descrição: ")
                print("Descrição atualizada com sucesso!")
                
                
                
                

                 
        