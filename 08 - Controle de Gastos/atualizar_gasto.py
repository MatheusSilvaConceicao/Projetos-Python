from registro import despesas
from datetime import datetime, date, time , timedelta



def atualizar_gasto():
    if not despesas:
        print("Você não possui gastos.")
    else:
        for i, gasto in enumerate(despesas, start=1):
            print(f"[{i}] {gasto['descricao']} - R${gasto['valor']:.2f}")
        
        num_gasto = int(input("Qual gasto você deseja atualizar? "))
        ind_gasto = num_gasto - 1
        
        if 0 <= ind_gasto < len(despesas):
            print(f"Descrição atual: {despesas[ind_gasto]['descricao']}")
            if input("Você deseja alterar a descrição? (S/N): ").lower() == "s":
                despesas[ind_gasto]['descricao'] = input("Digite a nova descrição: ")
                print("Descrição atualizada com sucesso!")
            else:
                print("Próximo item.")

            print(f"Valor atual: R${despesas[ind_gasto]['valor']:.2f}")
            if input("Você deseja alterar o valor? (S/N): ").lower() == "s":
                despesas[ind_gasto]['valor'] = float(input("Digite o novo valor: "))
                print("Valor atualizado com sucesso!")
            else:
                print("Próximo item.")

            print(f"Data atual: {despesas[ind_gasto]['data']}")
            if input("Você deseja alterar a data? (S/N): ").lower() == "s":
                despesas[ind_gasto]['data'] = input("Digite a nova data (DD/MM/AAAA): ")
                print("Data atualizada com sucesso!")
            else:
                print("Próximo item.")

            print(f"Categoria atual: {despesas[ind_gasto]['categoria']}")
            if input("Você deseja alterar a categoria? (S/N): ").lower() == "s":
                despesas[ind_gasto]['categoria'] = input("Digite a nova categoria: ")
                print("Categoria atualizada com sucesso!")
            else:
                print("Atualização concluída.")
        else:
            print("Número inválido. Tente novamente.")

                
                

                 
        