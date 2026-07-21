def resolver_dilema(escolha_jogador1, escolha_jogador2):
    # Usando os operadores relacionais da imagem que você enviou
    if escolha_jogador1 == 'cooperar' and escolha_jogador2 == 'cooperar':
        return "Ambos cooperaram: 3 pontos cada."
    elif escolha_jogador1 == 'trair' and escolha_jogador2 == 'trair':
        return "Ambos traíram: 1 ponto cada."
    elif escolha_jogador1 == 'trair' and escolha_jogador2 == 'cooperar':
        return "Jogador 1 traiu e ganhou 5 pontos! Jogador 2 cooperou e ganhou 0."
    elif escolha_jogador1 == 'cooperar' and escolha_jogador2 == 'trair':
        return "Jogador 2 traiu e ganhou 5 pontos! Jogador 1 cooperou e ganhou 0."
    else:
        return "Entrada inválida. Digite 'cooperar' ou 'trair'."

# Testando o sistema
print("--- Simulador do Dilema do Prisioneiro ---")
j1 = input("Escolha do Jogador 1 (cooperar/trair): ").lower()
j2 = input("Escolha do Jogador 2 (cooperar/trair): ").lower()

resultado = resolver_dilema(j1, j2)
print(resultado)