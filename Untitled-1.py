def sistema_financeiro():
    saldo = 0.0
    
    while True:
        print("\n--- MENU DE CONTROLE FINANCEIRO ---")
        print("1 - Registrar Entrada")
        print("2 - Consultar Saldo")
        print("3 - Encerrar")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Digite o valor a ser registrado: "))
                if valor > 0:
                    saldo += valor
                    print(f"R$ {valor:.2f} adicionado com sucesso.")
                else:
                    print("Valor deve ser positivo.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")
                
        elif opcao == "2":
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            
        elif opcao == "3":
            print("Encerrando o sistema. Até logo!")
            break  # Sai do loop while
            
        else:
            print("Opção inválida! Tente novamente.")

# Execução
sistema_financeiro()