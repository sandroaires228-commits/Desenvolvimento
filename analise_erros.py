"""
🔴 ERROS ENCONTRADOS - VALIDADOR DE ACESSO
===========================================
"""

print("""
┌─────────────────────────────────────────────────────────────┐
│                    ANÁLISE DE ERROS                         │
└─────────────────────────────────────────────────────────────┘

❌ ERRO 1: SINTAXE INVÁLIDA NA ÚLTIMA LINHA
─────────────────────────────────────────────
Localização: Última linha do código
Tipo: SyntaxError

CÓDIGO ERRADO:
    if __name__ == "__main__":
        validar_acesso() encontre possíveis erros=que o impeça de rodar esse código
                         ^^^^^^^^^^^^^^^^^^^^^^^ ^^^
                         TEXTO SOLTO INVÁLIDO    ATRIBUIÇÃO INVÁLIDA

Problema:
  • Após validar_acesso() há texto sem sentido
  • "encontre possíveis erros" não é comando Python válido
  • "=que o impeça de rodar esse código" parece uma atribuição malformada

Mensagem de Erro que Python exibiria:
  SyntaxError: invalid syntax
  
Solução:
    if __name__ == "__main__":
        validar_acesso()
                        ↑
                        Apenas isto. Sem nada depois.


⚠️ POSSÍVEL ERRO 2: LÓGICA DE MENSAGENS DUPLICADAS
──────────────────────────────────────────────────
Localização: Dentro do while

Código Original:
    while tentativas > 0:
        nome_usuario = input(...)
        
        if nome_usuario in MEMBROS_AUTORIZADOS:
            print("Acesso Liberado!")
            return True
            
        tentativas -= 1
        print("Acesso Negado. Tente novamente.")  # Sempre imprime
    
    print("Limite de tentativas excedido...")      # Sempre imprime

Problema:
  • A mensagem final é impressa FORA do loop
  • Se o usuário falhar e sair do loop, vê duas mensagens

Exemplo de execução:
    Tentativa 1: digita "maria" → "Acesso Negado"
    Tentativa 2: digita "jose"  → "Acesso Negado"
    Tentativa 3: digita "pedro" → "Acesso Negado"
    Depois sai do loop → "Limite de tentativas excedido"
    
Solução:
    Mover mensagem final para dentro do loop ou depois


✅ CÓDIGO CORRIGIDO E TESTADO:
──────────────────────────────
""")

# Dados configuráveis
MEMBROS_AUTORIZADOS = ["ana", "bruno", "carlos", "daniela", "sandro"]

def validar_acesso():
    """Valida acesso com limite de tentativas."""
    tentativas = 3
    
    while tentativas > 0:
        nome_usuario = input(f"\nDigite seu nome ({tentativas} tentativas): ").strip().lower()
        
        if nome_usuario in MEMBROS_AUTORIZADOS:
            print("✅ Acesso Liberado! Bem-vindo!\n")
            return True
        
        tentativas -= 1
        
        if tentativas > 0:
            print(f"❌ Acesso Negado. {tentativas} tentativas restantes.\n")
        else:
            print("❌ Limite de tentativas excedido. Contate o administrador.\n")
    
    return False

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🔐 SISTEMA DE VALIDAÇÃO DE ACESSO")
    print("="*50)
    print("Usuários válidos: ana, bruno, carlos, daniela, sandro\n")
    
    resultado = validar_acesso()
    
    if resultado:
        print("✅ Login bem-sucedido!")
    else:
        print("❌ Login falhou!")
