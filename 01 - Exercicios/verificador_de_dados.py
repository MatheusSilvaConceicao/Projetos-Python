#Peça ao usuário um valor e informe se é int, float ou str

valor = input("Digite algo: ")

try:
    valor = int(valor)
    tipo = "int"
except ValueError:
    try:
        valor = float(valor)
        tipo = "float"
    except ValueError:
        tipo = "str"
        
print(f"Você digitou {valor} e ele é um {tipo}")