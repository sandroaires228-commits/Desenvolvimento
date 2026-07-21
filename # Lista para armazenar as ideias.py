# Lista para armazenar as ideias
ideias = []

while True:
    print("\n--- PAINEL DE IDEIAS DA STARTUP ---")
    print("1 - Adicionar Ideia")
    print("2 - Listar Ideias")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nova_ideia = input("Digite a nova ideia de projeto: ")
        ideias.append(nova_ideia)
        print("Ideia registrada com sucesso!")
        
    elif opcao == "2":
        # Verifica se a lista está vazia
        if not ideias:
            print("Nenhuma ideia cadastrada até o momento.")
        else:
            print("\nLista de Ideias:")
            # enumerate cria um contador automático (start=1 ajusta para começar no 1)
            for i, ideia in enumerate(ideias, start=1):
                print(f"{i}. {ideia}")
                
    elif opcao == "3":
        print("Encerrando o painel. Boa sorte com os projetos!")
        break # Sai do loop while
        
    else:
        print("Opção inválida! Tente novamente.")