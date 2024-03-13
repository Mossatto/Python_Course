menu = """
=========== M E N U ===========

****** B E M - V I N D O ****** 
_______________________________

O P Ç Õ E S ----->
_______________________________

[D] - D E P Ó S I T O
[S] - S A Q U E
[E] - E X T R A T O
[X] - S A I R
_______________________________

===============================
"""

saldo = 0

limite = 500

extrato = ""

numeros_de_saque = 0

LIMITE_SAQUE = 3

continuar = True

while continuar:
    opcao = input(menu).upper()

    if opcao == "D":
        valor_do_deposito = float(input("Insira o valor do depósito: "))

        if valor_do_deposito <= 0:
            print("Insira um valor válido")
        saldo += valor_do_deposito
        extrato += f"Depósito no valor de R$ {valor_do_deposito:.2f}\n"

    elif opcao == "S":

        valor_do_saque = float(input("Insira o valor para saque: "))

        excedeu_o_saldo = valor_do_saque > saldo
        excedeu_o_limite = valor_do_saque > limite
        excedeu_quantidade_saques = numeros_de_saque > LIMITE_SAQUE

        if excedeu_o_saldo:
            print("Você não tem Saldo suficiente")

        elif excedeu_o_limite:
            print("Você excedeu seu limite de saque")
        
        elif excedeu_quantidade_saques:

            print("Você excedeu o número permitido de saques diários")
        
        elif valor_do_saque > 0:
        
            numeros_de_saque += 1
            saldo -= valor_do_saque
            extrato += f"Saque no valor de R${valor_do_saque:.2f}\n"        
        else:
            print("Algum erro ocorreu")

    elif opcao == "E":
        print("=========== EXTRATO ===========")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo : R${saldo:.2f}")
        print("==============================")

    elif opcao == "X":
        continuar = False
    
    else:
        print("Ocorreu um erro na aplicação")