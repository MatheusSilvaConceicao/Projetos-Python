from registro import pedir_descricao, data_despesa, pedir_descricao, registrar_Despesa, despesas
from listar import listar_despesas
from categorizar_gastos import categorizar_gastos
from excluir_gasto import excluir_gasto
from atualizar_gasto import atualizar_gasto

while True:
    
    try:
        print("""
        [1] - Adicionar Gastos
        [2] - Listar Gastos     
        [3] - Categorizar Gastos
        [4] - Excluir Gastos
        [0] - Sair          
            """)
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            registrar_Despesa()
        elif opcao == 2:
            listar_despesas()
        elif opcao == 3:
            categorizar_gastos()
        elif opcao == 4:
            excluir_gasto()
        elif opcao == 0:
            break
        else:
            print("Digite apenas numeros de 0 a 4.")
        
    except ValueError:
        print("Digite apenas números.")