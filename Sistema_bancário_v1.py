saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

print("----SEJA BEM VINDO----")

while True:
    
    print("\nDIGITE A OPÇÃO DESEJADA OU 4 PARA SAIR\n")

    print("""
           1 - Depósito
           2 - Saque
           3 - Extrato
           4 - sair
           """)
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao < 1 or opcao > 4:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
    
    if opcao == 1:
        deposito = float(input("Digite o valor que deseja depositar: R$  "))
        if deposito <=0:
            print("Valor de depósito invalido, tente novamente.")
        
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print(f"Seu saldo após o deposito é de {saldo:.2f}")
        
    elif opcao == 2:
        if numero_de_saques >= limite_de_saques:
            print("Número de saque diários excedidos")
            
        else:
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            if saque > saldo:
                print("Saldo insuficiente")
                
            elif saque > limite:
                print("Valor de saque excede o valor diário de R$ 500,00")
            
            else:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_de_saques += 1
                print(f"Seu saldo após o Saque é de {saldo:.2f}")
        
    if opcao == 3:
        print("\n----EXTRATO----")
        print("Não foram realizada movimentações."if not extrato.strip() else extrato)
        print (f"Saldo Atual: R$ {saldo:.2f}")
        print("-=-"*5)
        
    if opcao == 4:
        print ("OBRIGADO E VOLTE SEMPRE")
        break

