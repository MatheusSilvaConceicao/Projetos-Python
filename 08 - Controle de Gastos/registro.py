from datetime import datetime, date, time , timedelta

despesas = []

def pedir_valor():
    while True:
        try:
            valor = float(input("Qual o valor da despesa: "))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")
            
            
def data_despesa():
    while True:
        data = input("Digite a data da despesa (dd/mm/aaaa) ou deixe vazio para hoje: ")
        if not data:
            data = datetime.today().strftime("%d/%m/%Y")
            return data
        else:
            try:
                datetime.strptime(data, "%d/%m/%Y")
                return data
            except ValueError:
                print("Data inválida! Use o formato dd/mm/aaaa")     
                
                
def pedir_descricao():
    while True:
        descricao = input("Descreva a despesa (Ex: Condomínio, Netflix , Restaurante A): ").strip()
        if len(descricao) == 0:
            print("Descrição não pode ficar vazia.") 
        elif len(descricao) > 14:
            print("Descreva em apenas 14 caracteres")
        else:
            return descricao
             

def registrar_Despesa():
    
    try:
        print("""
        1 - Habitação 
        2 - Alimentação
        3 - Transporte
        4 - Outros     
            """)
        
        categorias = {
            1:"Habitação",
            2:"Alimentação",
            3:"Transporte",
            4:"Outros"
        }
        
        
        opcao_despesa = int(input("Digite a opção desejada: "))
        
        
        if opcao_despesa in categorias:
            categoria_nome = categorias[opcao_despesa]
            
            descricao_despesa = pedir_descricao()
            valor_despesa = pedir_valor()
            data = data_despesa() 
            
            despesa = {
                "categoria" : categoria_nome,
                "descricao" : descricao_despesa,
                "valor" : valor_despesa,
                "data" : data            
            }
            
            despesas.append(despesa)
            print("Despesa adicionada com sucesso!") 
        else:
            print("Digite um número entre 1 e 4")
    
    except ValueError:
        print("Digite apenas números.")