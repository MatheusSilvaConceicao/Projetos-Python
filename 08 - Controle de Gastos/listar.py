from registro import despesas
from datetime import datetime, date, time , timedelta

def listar_despesas():
    if not despesas:
        print("Nenhuma despesa registrada.")
    else:
        print("\nLISTA DE DESPESAS")
        print("=" * 30)
        for i, despesa in enumerate(despesas, start=1):
            print(f"[{i}]{despesa['descricao'].capitalize()} - R$ {despesa['valor']:.2f}")
            print(f"   Categoria: {despesa['categoria'].capitalize()}")
            print(f"   Data     : {despesa['data']}")
            print("-" * 30)