menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo, numero_saques = 0, 0
LIMITE = 500
LIMITE_SAQUE = 3
extrato = ""

while True:
    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor >= 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "S":
        valor = float(input("Informe o valor do depósito: "))

        if valor > LIMITE:
            print("Operação falhou! Valor do saque excede limite.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif numero_saques > LIMITE_SAQUE:
            print("Operação falhou! Número de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque...: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n*********************** EXTRATO ***********************")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*******************************************************")

    elif opcao == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente!")