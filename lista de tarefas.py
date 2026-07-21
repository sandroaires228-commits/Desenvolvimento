# 1. Criação da lista vazia
tarefas_sprint = []

# 2. Adicionando 4 tarefas usando .append()
tarefas_sprint.append("Configurar servidor em nuvem")
tarefas_sprint.append("Desenvolver o layout do protótipo")
tarefas_sprint.append("Criar banco de dados PostgreSQL")
tarefas_sprint.append("Implementar sistema de login")

# 3. Removendo uma tarefa cancelada com .remove()
# (O Python busca o valor exato dentro da lista e o remove)
tarefas_sprint.remove("Implementar sistema de login")

# 4. Imprimindo o total de tarefas com len()
total = len(tarefas_sprint)
print(f"Total de tarefas na Sprint: {total}")

# 5. Exibindo o quadro atualizado usando um loop for
print("\n=== Quadro de Tarefas da Startup ===")
for tarefa in tarefas_sprint:
    # A indentação aqui é crucial (4 espaços) conforme a PEP 8
    print(f"-> {tarefa}")
