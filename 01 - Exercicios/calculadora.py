#Calculadora
n = float(0)
n_user = " "

def verificar_opcao(n_user):
    while True:
        print("== Calculadora ==")
        print("A : ADIÇÃO")
        print("S : SUBTRAÇÃO")
        print("M : MULTIPLICAÇÃO")
        print("D : DIVISÃO")
        print("Z : ZERAR")
        print("# : SAIR")
        
       
        n_user = input("OPÇÃO: ").upper()
        
        match n_user:
            case "A":
                operacao_somar()
            case "S":
                operacao_subtrair()
            case "M":
                operacao_multiplicar()
            case "D":
                operacao_divisao()
            case "Z":
                operacao_zerar()
            case "#":
                print("ATÉ MAIS")
                break
            case _:
                print("OPÇÃO INVALIDA")



def operacao_somar():
    n_value = float(input("VALOR: "))
    global n
    n += n_value
    print(n)
    
 
def operacao_subtrair():
    n_value = float(input("VALOR: "))
    global n
    n -= n_value
    print(n)


def operacao_divisao():
    n_value = float(input("VALOR: "))
    global n
    n /= n_value
    print(n)
    
    
def operacao_multiplicar():
    n_value = float(input("VALOR: "))
    global n
    n *= n_value
    print(n)
    
    
def operacao_zerar():
    global n
    n = 0
    print(n)
    
verificar_opcao(n_user)