# 1. Dados configuráveis fora da lógica
MEMBROS_AUTORIZADOS = ["ana", "bruno", "carlos", "daniela", "sandro"]

def validar_acesso():
    """Gerencia a lógica de validação de acesso com limite de tentativas."""
    tentativas = 3
    
    while tentativas > 0:
        nome_usuario = input(f"Digite seu nome ({tentativas} tentativas): ").strip().lower()
        
        if nome_usuario in MEMBROS_AUTORIZADOS:
            print("  Acesso Liberado! Bem-vindo ao painel da Startup.")
            return True
        
        tentativas -= 1
        
        if tentativas > 0:
            print(f"❌ Acesso Negado. {tentativas} tentativas restantes.\n")
        else:
            print("❌ Limite de tentativas excedido. Contate o administrador.\n")
    
    return False

#  SINTAXE CORRETA
if __name__ == "__main__":
    validar_acesso()