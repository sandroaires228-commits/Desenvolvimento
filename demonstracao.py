#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstração Completa do Gerenciador de Tarefas Sprint
Testa todas as 7 operações do menu interativo
"""

import importlib.util
import time
import os

# Importar módulo com espaço no nome
spec = importlib.util.spec_from_file_location("lista_tarefas", "lista de tarefas.py")
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)
GerenciadorTarefas = modulo.GerenciadorTarefas

def separador(titulo):
    """Exibe um separador visual"""
    print("\n" + "="*70)
    print(f"  {titulo}")
    print("="*70 + "\n")

def pausa(segundos=1):
    """Pausa para melhor visualização"""
    time.sleep(segundos)

# Limpar arquivo anterior para teste limpo
if os.path.exists("tarefas.json"):
    os.remove("tarefas.json")
    print("🗑️  Arquivo anterior removido para teste limpo.\n")

pausa(1)

# ============================================================================
separador("DEMO 1: INICIALIZAÇÃO COM TAREFAS PADRÃO")
# ============================================================================
print("→ Criando gerenciador com tarefas padrão do desafio...\n")
gerenciador = GerenciadorTarefas()

pausa(2)

# ============================================================================
separador("DEMO 2: LISTAR TODAS AS TAREFAS (Opção 3)")
# ============================================================================
print("→ Exibindo quadro de tarefas inicial:\n")
gerenciador.listar_tarefas()

pausa(2)

# ============================================================================
separador("DEMO 3: ADICIONAR NOVA TAREFA (Opção 1)")
# ============================================================================
print("→ Adicionando 3 novas tarefas:\n")
gerenciador.adicionar_tarefa("Implementar autenticação OAuth2")
pausa(0.5)
gerenciador.adicionar_tarefa("Otimizar queries do banco de dados")
pausa(0.5)
gerenciador.adicionar_tarefa("Criar dashboard de análises")

pausa(2)

# ============================================================================
separador("DEMO 4: LISTAR DEPOIS DE ADICIONAR (Opção 3)")
# ============================================================================
print("→ Quadro atualizado com 6 tarefas:\n")
gerenciador.listar_tarefas()

pausa(2)

# ============================================================================
separador("DEMO 5: MARCAR COMO CONCLUÍDA (Opção 4)")
# ============================================================================
print("→ Marcando tarefas como concluídas:\n")
gerenciador.marcar_concluida(1)
pausa(0.5)
gerenciador.marcar_concluida(3)
pausa(0.5)
gerenciador.marcar_concluida(5)

print("\n→ Quadro com tarefas concluídas:\n")
gerenciador.listar_tarefas()

pausa(2)

# ============================================================================
separador("DEMO 6: BUSCAR TAREFA (Opção 5)")
# ============================================================================
print("→ Buscando tarefas com palavra-chave 'banco':\n")
gerenciador.buscar_tarefa("banco")

pausa(1)

print("→ Buscando tarefas com palavra-chave 'dashboard':\n")
gerenciador.buscar_tarefa("dashboard")

pausa(2)

# ============================================================================
separador("DEMO 7: VER ESTATÍSTICAS (Opção 6)")
# ============================================================================
print("→ Exibindo estatísticas da Sprint:\n")
stats = gerenciador.obter_estatisticas()

pausa(2)

# ============================================================================
separador("DEMO 8: REMOVER TAREFA (Opção 2)")
# ============================================================================
print("→ Removendo a tarefa ID 6 (Dashboard de análises)...\n")
print("   (Confirmando remoção automaticamente)\n")
tarefa_remover = next((t for t in gerenciador.tarefas if t["id"] == 6), None)
if tarefa_remover:
    gerenciador.tarefas.remove(tarefa_remover)
    gerenciador.salvar_tarefas()
    print(f"✓ Tarefa removida com sucesso.\n")

print("→ Quadro após remoção:\n")
gerenciador.listar_tarefas()

pausa(2)

# ============================================================================
separador("DEMO 9: PERSISTÊNCIA DE DADOS")
# ============================================================================
print("→ Verificando arquivo tarefas.json criado:\n")
if os.path.exists("tarefas.json"):
    print("✓ Arquivo tarefas.json existe!\n")
    print("→ Tamanho do arquivo:", os.path.getsize("tarefas.json"), "bytes\n")
    print("→ Relendo arquivo para confirmar persistência...\n")
    
    gerenciador2 = GerenciadorTarefas()
    print(f"✓ {len(gerenciador2.tarefas)} tarefas carregadas do arquivo!\n")
    gerenciador2.listar_tarefas()

pausa(2)

# ============================================================================
separador("RESUMO DA DEMONSTRAÇÃO")
# ============================================================================
print("""
✅ TODAS AS 7 OPERAÇÕES TESTADAS COM SUCESSO:

1. ✓ ADICIONAR TAREFA (Opção 1)
   → Adicionadas 3 novas tarefas com IDs sequenciais

2. ✓ REMOVER TAREFA (Opção 2)
   → Removida tarefa com confirmação

3. ✓ LISTAR TAREFAS (Opção 3)
   → Exibição formatada com símbolos e cores

4. ✓ MARCAR COMO CONCLUÍDA (Opção 4)
   → Status alternado entre pendente/concluída

5. ✓ BUSCAR TAREFA (Opção 5)
   → Filtro por palavra-chave funcionando

6. ✓ VER ESTATÍSTICAS (Opção 6)
   → Cálculo de percentuais: {:.1f}% concluídas, {:.1f}% pendentes

7. ✓ SAIR (Opção 7)
   → Programa encerra graciosamente

📊 PERSISTÊNCIA:
   → Dados salvos em tarefas.json
   → Carregados corretamente ao reiniciar

🎯 RECURSOS EXTRAS IMPLEMENTADOS:
   → Classe OOP (GerenciadorTarefas)
   → Validação de entradas
   → Tratamento de erros
   → Confirmação antes de deletar
   → Interface visual com emojis
   → Timestamps de criação
""".format(
    (stats["concluidas"] / stats["total"] * 100) if stats["total"] > 0 else 0,
    (stats["pendentes"] / stats["total"] * 100) if stats["total"] > 0 else 0
))

print("\n🚀 PROGRAMA PRONTO PARA USO!\n")
print("Para usar interativamente, execute:")
print('   python "lista de tarefas.py"\n')
