def obter_faturamento():
    while True:
        try:
            texto = input("Digite o faturamento mensal (ex: 1.000,00): ")
            texto = texto.replace(".", "").replace(",", ".")
            return float(texto)
        except ValueError:
            print("Entrada inválida. Por favor, digite o número usando apenas números, ponto e vírgula.")

nome_empresa = input("Digite o nome da empresa: ")
faturamento_mensal = obter_faturamento()

while True:
    try:
        quantidade_funcionarios = int(input("Digite a quantidade de funcionários: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido para funcionários.")

faturamento_anual = faturamento_mensal * 12

# Formatação personalizada para o padrão brasileiro
faturamento_formatado = f"{faturamento_anual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(f"\n--- Cadastro concluído ---")
print(f"A empresa {nome_empresa} com {quantidade_funcionarios} funcionários "
      f"projeta um faturamento anual de R$ {faturamento_formatado}.")