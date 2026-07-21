# 1. Criar uma lista vazia
tarefas_sprint = []

# 2. Adicionar 4 tarefas
tarefas_sprint.append("Criar tela de login")
tarefas_sprint.append("Implementar cadastro de usuários")
tarefas_sprint.append("Corrigir bug no botão de pagamento")
tarefas_sprint.append("Escrever documentação da API")

# 3. Remover a tarefa cancelada
tarefas_sprint.remove("Corrigir bug no botão de pagamento")

# 4. Imprimir o total de tarefas
print("Total de tarefas:", len(tarefas_sprint))

# 5. Exibir o quadro atualizado
print("\nQuadro atualizado:")
for tarefa in tarefas_sprint:
    print("-", tarefa)