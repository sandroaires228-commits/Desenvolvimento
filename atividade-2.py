def calcular_divisao():
    print("--- Divisor de Despesas da Startup ---")
    
    # Bloco para garantir que o valor da conta seja um número válido
    while True:
        try:
            valor_conta = float(input("Digite o valor total da conta (ex: 150.50): "))
            if valor_conta < 0:
                print("O valor não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número usando ponto para decimais.")

    # Bloco para garantir que a quantidade de membros seja um inteiro válido
    while True:
        try:
            num_membros = int(input("Quantas pessoas vão dividir essa conta? "))
            if num_membros <= 0:
                print("A quantidade de membros deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Cálculo da divisão
    valor_por_pessoa = valor_conta / num_membros

    # Exibição do resultado
    print("-" * 35)
    print(f"Valor total da conta: R$ {valor_conta:,.2f}")
    print(f"Número de membros: {num_membros}")
    print(f"Cada um deve pagar: R$ {valor_por_pessoa:,.2f}")
    print("-" * 35)

# Chamada da função
if __name__ == "__main__":
    calcular_divisao()