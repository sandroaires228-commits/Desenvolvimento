"""
ANÁLISE DE ERROS - Validador de Acesso
======================================

Seu código tem ERROS que impedem a execução:
"""

# ❌ ERRO 1: Sintaxe inválida na última linha
# Código ERRADO:
# if __name__ == "__main__":
#     validar_acesso() encontre possíveis erros=que o impeça de rodar esse código
#                      ^^^^^^^^^^^^^^^^^^^^^^^ ERRO DE SINTAXE!

# Problema: texto solto + atribuição inválida
# Solução: remover o texto solto

# ✅ CÓDIGO CORRETO:

# 1. Dados configuráveis fora da lógica (mais fácil de gerenciar)
MEMBROS_AUTORIZADOS = ["ana", "bruno", "carlos", "daniela", "sandro"]

def validar_acesso():
    """Gerencia a lógica de validação de acesso com limite de tentativas."""
    tentativas = 3
    
    while tentativas > 0:
        # 2. .strip() remove espaços acidentais antes/depois do nome
        nome_usuario = input(f"Digite seu nome ({tentativas} tentativas restantes): ").strip().lower()
        
        if nome_usuario in MEMBROS_AUTORIZADOS:
            print("✓ Acesso Liberado! Bem-vindo ao painel da Startup.")
            return True  # Retorna True para indicar sucesso
        
        tentativas -= 1
        if tentativas > 0:
            print("✗ Acesso Negado. Tente novamente.")
        else:
            print("✗ Limite de tentativas excedido. Contate o administrador.")
    
    return False

# Execução do sistema (SINTAXE CORRETA)
if __name__ == "__main__":
    validar_acesso()
