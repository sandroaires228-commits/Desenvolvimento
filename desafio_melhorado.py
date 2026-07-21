# ============================================================================
# GERENCIADOR DE TAREFAS - VERSÃO MELHORADA (Desafio Sprint 1)
# Mantém os conceitos: Lista, append(), remove(), len(), loop for
# ============================================================================

def exibir_menu():
    """Exibe menu de opções."""
    print("\n" + "="*50)
    print("📋 GERENCIADOR DE TAREFAS")
    print("="*50)
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Ver total de tarefas")
    print("5. Sair")
    print("="*50)

def adicionar_tarefa(tarefas):
    """Adiciona uma tarefa à lista usando append()."""
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print(f"✓ Tarefa adicionada!\n")
    else:
        print("✗ Tarefa não pode estar vazia.\n")

def remover_tarefa(tarefas):
    """Remove uma tarefa da lista usando remove()."""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    tarefa = input("Digite a tarefa a remover: ").strip()
    if tarefa in tarefas:
        tarefas.remove(tarefa)  # remove() busca valor exato
        print(f"✓ Tarefa removida!\n")
    else:
        print(f"✗ Tarefa não encontrada.\n")

def listar_tarefas(tarefas):
    """Lista todas as tarefas usando loop for."""
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.\n")
        return
    
    print("\n" + "="*50)
    print("📋 QUADRO DE TAREFAS DA STARTUP")
    print("="*50)
    
    # 5. Exibindo tarefas usando loop for
    for i, tarefa in enumerate(tarefas, 1):
        print(f"  {i}. {tarefa}")
    
    print("="*50 + "\n")

def exibir_total(tarefas):
    """Exibe o total de tarefas usando len()."""
    # 4. Imprimindo o total de tarefas com len()
    total = len(tarefas)
    print(f"\n📊 Total de tarefas na Sprint: {total}\n")

def menu_principal():
    """Menu interativo do programa."""
    
    # 1. Criação da lista vazia
    tarefas_sprint = []
    
    # 2. Adicionando 4 tarefas usando .append()
    tarefas_padrao = [
        "Configurar servidor em nuvem",
        "Desenvolver o layout do protótipo",
        "Criar banco de dados PostgreSQL",
        "Implementar sistema de login"
    ]
    
    for tarefa in tarefas_padrao:
        tarefas_sprint.append(tarefa)
    
    print("✓ Tarefas padrão carregadas.\n")
    
    # 3. Removendo uma tarefa cancelada com .remove()
    tarefas_sprint.remove("Implementar sistema de login")
    print("✓ Tarefa 'Implementar sistema de login' removida.\n")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            adicionar_tarefa(tarefas_sprint)
        elif opcao == "2":
            remover_tarefa(tarefas_sprint)
        elif opcao == "3":
            listar_tarefas(tarefas_sprint)
        elif opcao == "4":
            exibir_total(tarefas_sprint)
        elif opcao == "5":
            print("\n👋 Até logo!\n")
            break
        else:
            print("✗ Opção inválida. Digite 1-5.\n")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.\n")
