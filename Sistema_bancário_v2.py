from datetime import datetime

saldo = 0
limite = 500
extrato = ""
numero_transações = 0
limite_transações = 10
movimentacoes = [] # Lisata para armazenar as movimentações com horário

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
        
        if numero_transações >= limite_transações:
            print("Número transações diárias excedidas")
        
        elif deposito <=0:
            print("Valor de depósito invalido, tente novamente.")
        
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            horario = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            movimentacoes.append(f"Depósito: R$ {deposito:.2f} - {horario}")
            numero_transações += 1
            print(f"Seu saldo após o deposito é de {saldo:.2f}")
            print(f"Você ainda tem {limite_transações - numero_transações} transações restantes para o dia de hoje")
            
        
    elif opcao == 2:
        if numero_transações >= limite_transações:
            print("Número transações diárias excedidas")
            
        else:
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            if saque > saldo:
                print("Saldo insuficiente")
                
            elif saque > limite:
                print("Valor de saque excede o valor diário de R$ 500,00")
            
            else:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                horario = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                movimentacoes.append(f"Saque: R$ {saque:.2f} - {horario}")
                numero_transações += 1
                print(f"Seu saldo após o Saque é de {saldo:.2f}")
                print(f"Você ainda tem {limite_transações - numero_transações} transações restantes para o dia de hoje")
        
    if opcao == 3:
        print("\n----EXTRATO----")
        if not movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            for mov in movimentacoes:  # Exibe todas as movimentações com os horários registrados
                print(mov)
        print (f"Saldo Atual: R$ {saldo:.2f}")
        print("-=-"*5)
        
    if opcao == 4:
        print ("OBRIGADO E VOLTE SEMPRE")
        break

