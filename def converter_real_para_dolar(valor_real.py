def converter_real_para_dolar(valor_real, cotacao_dolar):
    """Converte Reais para Dólares usando a cotação fornecida."""
    return valor_real / cotacao_dolar


def ler_valor_numerico(mensagem, minimo=None, permitir_zero=False):
    """Lê um valor numérico do usuário com validação e tratamento de vírgula."""
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue

        entrada = entrada.replace("R$", "").replace("$", "").replace(" ", "").replace(",", ".")

        try:
            valor = float(entrada)
        except ValueError:
            print("Valor inválido. Use apenas números, ponto ou vírgula.")
            continue

        if not permitir_zero and valor == 0:
            print("O valor não pode ser zero. Digite um número diferente de zero.")
            continue

        if minimo is not None and valor < minimo:
            print(f"O valor precisa ser maior ou igual a {minimo}.")
            continue

        return valor


def main():
    print("--- Conversor Financeiro da Startup ---")
    try:
        valor = ler_valor_numerico("Digite o valor em R$: ", minimo=0.01)
        cotacao = ler_valor_numerico("Digite a cotação do dólar hoje: ", minimo=0.0001)

        resultado = converter_real_para_dolar(valor, cotacao)

        print(f"\nValor convertido: US$ {resultado:,.2f}")
        print(f"Entrada: R$ {valor:,.2f} | Cotação: {cotacao:.4f}")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário. Saindo...")


if __name__ == "__main__":
    main()