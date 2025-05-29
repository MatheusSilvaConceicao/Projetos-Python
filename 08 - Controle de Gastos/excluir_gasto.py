from registro import pedir_descricao, data_despesa, pedir_descricao, registrar_Despesa, despesas
from listar import listar_despesas
from categorizar_gastos import categorizar_gastos

def excluir_gasto():
    if not despesas:
        print("Você não possui gastos! ")
    else:
        print("======= EXCLUIR GASTO ======")
        for i, gasto in enumerate(despesas, start=1):
            print(30 * "=")
            print(f"[{i}] {gasto['descricao']} - R${gasto['valor']:.2f}")
            for chave, valor in gasto.items():
                if isinstance(valor,(int, float)):
                    print(f"{chave.capitalize():<10} - R${valor:.2f}")
                else:
                    print(f"{chave.capitalize():<10} - {valor}")
            
        opcao = int(input("Qual gasto você deseja excluir ?"))
            
        if 1 <= opcao <= len(despesas):
            despesas.pop(opcao - 1)
            print("Gasto excluído com sucesso !")
        else:
            print("Digite apenas números.")            