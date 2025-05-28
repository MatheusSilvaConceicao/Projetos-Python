from listar import listar_despesas
from registro import despesas
from datetime import datetime, date, time , timedelta

def categorizar_gastos():
    totais = dict() 
    if not despesas:
        print("Nenhum gasto registrado!")
    else:
        print("\nGASTOS POR CATEGORIA")
        print("=" * 30)
        for despesa in despesas:
            categoria = despesa["categoria"]
            valor = despesa["valor"]
            if categoria in totais:
                totais[categoria] += valor
            else:
                totais[categoria] = valor
            
        for categoria , valor in totais.items():
            print(f"{categoria.capitalize():<15} : R${valor:.2f}")