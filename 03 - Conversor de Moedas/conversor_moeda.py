# Função que realiza a conversão de moedas
def converter(cota, moeda):
    while True:
        try:
            # Solicita ao usuário um valor em reais (BRL) e converte para float
            valor1 = float(input("QUAL O VALOR R$? "))
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("Erro! Digite um valor numérico válido.")  # Exibe erro se a entrada não for um número
    
    print("========================")
    cotacao = valor1 * cota  # Calcula o valor convertido com base na cotação
    print(f"R$ {valor1:.2f} -> {moeda} {cotacao:.2f}")  # Exibe o resultado formatado
    print("========================")

while True:
    print('''
    ======= CONVERSOR DE MOEDAS =======  
    01 - DÓLAR (USD)
    02 - EURO   (EUR)
    03 - LIBRA ESTERLINA  (GBP)  
    04 - SAIR 
    ===================================
    ''')

    try:
        opcao = int(input("ESCOLHA UMA OPÇÃO: "))  # Lê a opção escolhida pelo usuário
    except ValueError:
        print("Erro! Digite um número válido.")  # Trata entradas inválidas
        continue  # Retorna ao menu

    # Estrutura match-case para tratar a escolha do usuário
    match opcao:
        case 1:
            converter(0.17, "USD$")  # Chama a função para converter para Dólar
        case 2:
            converter(0.16, "EUR€")  # Chama a função para converter para Euro
        case 3:
            converter(0.13, "GBP£")  # Chama a função para converter para Libra Esterlina
        case 4:
            break  # Sai do loop e encerra o programa
        case _:
            print("Opção inválida! Escolha um número entre 1 e 4.")  # Trata opções inválidas
            
    input("\nPressione ENTER para continuar...")  # Aguarda o usuário antes de voltar ao menu
