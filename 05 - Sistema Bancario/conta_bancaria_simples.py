from datetime import datetime


# Variáveis globais usadas para armazenar informações da conta
conta = 0  # Saldo inicial da conta
extrato = []  # Lista que armazena o histórico de transações
LIMITE_SAQUE = 3  # Quantidade máxima de saques por dia
LIMITE_VALOR_SAQUE = 500.00  # Valor máximo permitido por saque
n_transacoes = 0
data_atual = datetime.now()
mascara_ptbr = "%d-%m-%Y %H:%M"

# Função responsável por realizar depósitos na conta


def deposito_conta(saldo, historico, n_transacoes , data_atual):
    if n_transacoes < 10:
        # Solicita o valor do depósito ao usuário
        deposito = float(input("QUAL VALOR VOCÊ DESEJA DEPOSITAR : "))
        if deposito > 0:  # Verifica se o valor do depósito é positivo
            saldo += deposito  # Adiciona o valor ao saldo
            data_atual = datetime.now()
            # Registra a operação no extrato
            historico.append(f"DEPÓSITO: +R$ {deposito:.2f} - {data_atual.strftime(mascara_ptbr)}")
            print(f"DEPÓSITO DE R$ {deposito:.2f} REALIZADO COM SUCESSO! - {data_atual.strftime(mascara_ptbr)}")
            n_transacoes += 1
        else:
            # Exibe mensagem de erro caso o valor seja inválido
            print("DIGITE UM VALOR POSITIVO")
    else:
        print(f"Você atingiu o limite de transações diárias - {data_atual.strftime(mascara_ptbr)}")
    return saldo, historico, n_transacoes , data_atual# Retorna o saldo atualizado e o histórico de transações
    

# Função responsável por realizar saques na conta


def saque_conta(saldo, historico, n_transacoes, data_atual):
    if n_transacoes < 10:
        # Solicita o valor do saque
        saque = float(input("QUAL O VALOR DO SAQUE: "))
        if saque > 0 and saque <= LIMITE_VALOR_SAQUE:  # Garante que o saque esteja dentro do limite permitido
            if saque <= saldo:  # Verifica se há saldo suficiente para o saque
                saldo -= saque  # Deduz o valor do saldo
                # Registra a operação no extrato
                historico.append(f"SAQUE:    -R$ {saque:.2f}  - {data_atual.strftime(mascara_ptbr)}")
                n_transacoes += 1 
                data_atual = datetime.now()# Incrementa o contador de saques realizados
                print(f"SAQUE DE R$ {saque:.2f} REALIZADO COM SUCESSO! - {data_atual.strftime(mascara_ptbr)}")
            else:
                # Exibe mensagem de erro caso não haja saldo suficiente
                print("SALDO INSUFICIENTE!")
                print(f"SALDO ATUAL: R$ {conta:.2f} - {data_atual.strftime(mascara_ptbr)}")  # Exibe o saldo atual
        else:
            # Mensagem de erro caso o valor do saque ultrapasse o limite
            print("LIMITE DE SAQUE: R$ 500,00")
    else:
        print("Você atingiu o número de transações diárias")
    # Retorna o saldo atualizado, o histórico e o número de saques realizados
    return saldo, historico, n_transacoes, data_atual

# Função responsável por exibir o extrato da conta


def extrato_conta(saldo,historico, data_atual):
    print("===== EXTRATO =====\n")
    if not historico:  # Verifica se houve movimentação na conta
        # Exibe mensagem caso não haja transações registradas
        print("NENHUMA MOVIMENTAÇÃO")
    else:
        for movimento in historico:  # Percorre e exibe todas as transações realizadas
            print(movimento)
            data_atual = datetime.now()
        # Exibe o saldo atual da conta
        print(f"\nSALDO ATUAL: R$ {conta:.2f} - {data_atual.strftime(mascara_ptbr)}")
    print("====================")



# Loop principal do programa para interação com o usuário
while True:
    print('''
        
        ==== BEM VINDO ====
        [1] - DEPÓSITO
        [2] - SAQUE
        [3] - EXTRATO
        [0] - SAIR 
        ===================  
        ''')

    # Usuário escolhe uma opção do menu
    opcao = int(input("Digite a opção desejada : "))

    # Verifica a opção escolhida e chama a função correspondente
    if opcao == 1:
        conta, extrato , n_transacoes, data_atual = deposito_conta(conta, extrato,n_transacoes,data_atual)  # Chama a função de depósito
    elif opcao == 2:
        conta , extrato, n_transacoes,data_atual = saque_conta(conta, extrato, n_transacoes, data_atual)  # Chama a função de saque
    elif opcao == 3:
        extrato_conta(conta, extrato,data_atual)  # Chama a função de extrato
    elif opcao == 0:
        break  # Encerra o programa caso o usuário escolha sair
    else:
        # Exibe mensagem de erro caso a opção seja inválida
        print("Digite uma opção válida")
