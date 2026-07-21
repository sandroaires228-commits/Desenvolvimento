def solicitar_texto(prompt):
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Entrada inválida. Por favor, digite um texto não vazio.")


def solicitar_inteiro(prompt, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(prompt))
            if minimo is not None and valor < minimo:
                print(f"Valor inválido. O número deve ser maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor inválido. O número deve ser menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def solicitar_decimal(prompt, minimo=None):
    while True:
        try:
            valor = float(input(prompt).replace(',', '.'))
            if minimo is not None and valor < minimo:
                print(f"Valor inválido. O número deve ser maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


def solicitar_sim_nao(prompt):
    while True:
        valor = input(prompt).strip().lower()
        if valor in {'1', 's', 'sim'}:
            return True
        if valor in {'0', 'n', 'nao', 'não'}:
            return False
        print("Resposta inválida. Digite 1/Sim ou 0/Não.")


def exibir_relatorio(dados):
    print("\n--- Relatório de Perfil da Startup ---")
    print(f"Nome da Empresa: {dados['nome']}")
    print(f"Número de Sócios: {dados['socios']}")
    print(f"Faturamento Projetado: R$ {dados['faturamento']:,.2f}")
    print(f"Protótipo no ar: {'Sim' if dados['prototipo'] else 'Não'}")


def main():
    print("# Ficha Técnica de Startup")
    nome = solicitar_texto("Digite o nome da Startup: ")
    socios = solicitar_inteiro("Digite a quantidade de sócios: ", minimo=1)
    faturamento = solicitar_decimal("Digite o faturamento mensal previsto: R$ ", minimo=0)
    possui_prototipo = solicitar_sim_nao("Já possui protótipo? (1 para Sim / 0 para Não): ")

    startup_dados = {
        "nome": nome,
        "socios": socios,
        "faturamento": faturamento,
        "prototipo": possui_prototipo
    }

    exibir_relatorio(startup_dados)


if __name__ == "__main__":
    main()