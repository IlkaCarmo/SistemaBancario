print("Seja bem vindo ao banco Picpay")

menu = """
[1] Sacar
[2] Depositar   
[3] Extrato
[4] Sair
=>"""

saldo = 10000
limite_saque_diario = 500
saques_diarios = 3
numero_saques = 0
extrato = []


while True:
    opcao_escolhida = input(menu)

    if opcao_escolhida == "1":
        print("Qual valor deseja sacar?")
        valor_saque = float(input())
        if valor_saque > saldo:
            print("Saldo insuficiente para saque")
        elif numero_saques  >= saques_diarios:
            print("Limite de saques diários atingido")
        elif valor_saque > limite_saque_diario:
            print("Valores de saque acima  de R$ 500,00 não são permitidos")
        else:
            saldo -= valor_saque
            saques_diarios -= 1
            numero_saques += 1
            extrato.append(f"Saque: -R$ {valor_saque:.2f}")
            print(f"Saque de {valor_saque} realizado com sucesso.")
            print(f"Saques restantes hoje: {saques_diarios}")

    elif opcao_escolhida == "2":
        print("Qual valor deseja depositar?")
        valor_deposito = float(input())
        if valor_deposito <= 0:
            print("Valor de depósito inválido. Tente novamente.")
        else:
            saldo += valor_deposito   
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
            print(f"Depósito de {valor_deposito} realizado com sucesso.")

    elif opcao_escolhida == "3":
        print("\n=========== EXTRATO =============")
        for transacao in extrato:
            print(f"{transacao}")

        print(f"Saldo atual: R$ {saldo:.2f}")
        print("\n=================================")

    elif opcao_escolhida == "4":
        print("Volte sempre")
        break
    else:
        print("Opção inválida. Por favor selecione uma opção válida.")
