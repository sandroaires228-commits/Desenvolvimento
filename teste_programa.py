#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script simples para testar o programa de tarefas"""

import sys
import importlib.util

# Importar módulo com espaço no nome
spec = importlib.util.spec_from_file_location("lista_tarefas", "lista de tarefas.py")
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)
GerenciadorTarefas = modulo.GerenciadorTarefas

# Teste 1: Carregar/inicializar tarefas
print("=" * 60)
print("TESTE 1: Inicialização")
print("=" * 60)
gerenciador = GerenciadorTarefas()

# Teste 2: Listar tarefas iniciais
print("\n" + "=" * 60)
print("TESTE 2: Listar tarefas iniciais")
print("=" * 60)
gerenciador.listar_tarefas()

# Teste 3: Adicionar nova tarefa
print("=" * 60)
print("TESTE 3: Adicionar nova tarefa")
print("=" * 60)
gerenciador.adicionar_tarefa("Testar sistema de notificações")

# Teste 4: Listar após adição
print("=" * 60)
print("TESTE 4: Listar após adição")
print("=" * 60)
gerenciador.listar_tarefas()

# Teste 5: Marcar como concluída
print("=" * 60)
print("TESTE 5: Marcar tarefa como concluída")
print("=" * 60)
gerenciador.marcar_concluida(1)
gerenciador.listar_tarefas()

# Teste 6: Buscar tarefa
print("=" * 60)
print("TESTE 6: Buscar por palavra-chave 'servidor'")
print("=" * 60)
gerenciador.buscar_tarefa("servidor")

# Teste 7: Estatísticas
print("=" * 60)
print("TESTE 7: Ver estatísticas")
print("=" * 60)
gerenciador.obter_estatisticas()

print("\n✓ Todos os testes executados com sucesso!")
