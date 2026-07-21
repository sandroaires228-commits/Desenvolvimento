def solicitar_texto(prompt):
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Entrada inválida. Por favor, digite um texto não vazio.")


def solicitar_decimal(prompt, minimo=None):
    while True:
        try:
            texto = input(prompt).strip().replace(',', '.')
            valor = float(texto)
            if minimo is not None and valor < minimo:
                print(f"Valor inválido. Digite um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: o valor deve ser um número válido.")


def exibir_menu():
    print("\n=== GERENCIADOR DE INOVAÇÃO ===")
    print("1 - Cadastrar Ideia Completa")
    print("2 - Listar Projetos e Faturamento")
    print("3 - Sair")


def cadastrar_projeto():
    print("\n--- Cadastro de Projeto ---")
    nome = solicitar_texto("Nome do Projeto: ")
    area = solicitar_texto("Área de Atuação: ")
    faturamento = solicitar_decimal("Faturamento Estimado: R$ ", minimo=0)

    projeto = {
        "nome": nome,
        "area": area,
        "faturamento": faturamento
    }

    print("Sucesso: Projeto registrado!")
    return projeto


def listar_projetos(projetos):
    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    total_acumulado = sum(p["faturamento"] for p in projetos)
    print(f"\n{'Projeto':<25} | {'Área':<20} | {'Faturamento'}")
    print("-" * 65)

    for p in projetos:
        print(f"{p['nome']:<25} | {p['area']:<20} | R$ {p['faturamento']:,.2f}")

    print("-" * 65)
    print(f"Faturamento Total Acumulado: R$ {total_acumulado:,.2f}")


def main():
    projetos_registrados = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            projeto = cadastrar_projeto()
            projetos_registrados.append(projeto)

        elif opcao == "2":
            listar_projetos(projetos_registrados)

        elif opcao == "3":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()