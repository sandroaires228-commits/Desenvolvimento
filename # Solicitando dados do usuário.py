# Solicitando dados do usuário
valor_compra = float(input("Digite o valor total da compra: R$ "))
cupom = input("Digite o nome do cupom (ou pressione Enter para pular): ").strip().upper()

# Lógica de decisão
if cupom == "STARTUP10":
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Cupom aplicado! Desconto de 10%.")
    print(f"O novo preço é: R$ {valor_final:.2f}")

elif cupom == "QUEROANUIDADE":
    print("Desconto especial de plano anual ativado!")
    print(f"Valor a pagar: R$ {valor_compra:.2f}")

else:
    # Caso qualquer outro cupom ou vazio
    print("Cupom inválido ou não informado.")
    print(f"Valor original da compra: R$ {valor_compra:.2f}")