import json
from dataclasses import asdict, dataclass
from pathlib import Path

DATA_FILE = Path("projetos.json")


@dataclass
class Projeto:
    nome: str
    area: str
    faturamento: float

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Projeto":
        return cls(
            nome=str(data.get("nome", "")),
            area=str(data.get("area", "")),
            faturamento=float(data.get("faturamento", 0.0)),
        )


def carregar_projetos() -> list[Projeto]:
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return [Projeto.from_dict(item) for item in dados]
    except (json.JSONDecodeError, OSError) as erro:
        print("Falha ao carregar os projetos. Iniciando com lista vazia.")
        print(f"Detalhes do erro: {erro}")
        return []


def salvar_projetos(projetos: list[Projeto]) -> None:
    try:
        with DATA_FILE.open("w", encoding="utf-8") as arquivo:
            json.dump([projeto.to_dict() for projeto in projetos], arquivo, ensure_ascii=False, indent=2)
    except OSError as erro:
        print("Erro ao salvar os projetos.")
        print(f"Detalhes do erro: {erro}")


def ler_texto(mensagem: str, campo: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print(f"{campo} não pode ficar vazio. Tente novamente.")


def ler_valor_numerico(mensagem: str, minimo: float = 0.0) -> float:
    while True:
        entrada = input(mensagem).strip().replace("R$", "").replace("$", "").replace(" ", "").replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Valor inválido. Informe um número válido.")
            continue

        if valor < minimo:
            print(f"O valor precisa ser maior ou igual a {minimo:,.2f}.")
            continue

        return valor


def exibir_menu() -> str:
    print("\n--- Sistema de Gestão de Projetos ---")
    print("1 - Cadastrar Projeto")
    print("2 - Listar Projetos")
    print("3 - Sair")
    return input("Escolha uma opção: ").strip()


def cadastrar_projeto(projetos: list[Projeto]) -> None:
    print("\n--- Cadastro de Projeto ---")
    nome = ler_texto("Nome do projeto: ", "Nome do projeto")
    area = ler_texto("Área de atuação: ", "Área de atuação")
    faturamento = ler_valor_numerico("Faturamento estimado: R$ ", minimo=0.0)

    novo_projeto = Projeto(nome=nome, area=area, faturamento=faturamento)
    projetos.append(novo_projeto)
    salvar_projetos(projetos)
    print("Projeto cadastrado com sucesso!")


def listar_projetos(projetos: list[Projeto]) -> None:
    print("\n--- Projetos Cadastrados ---")
    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    for indice, projeto in enumerate(projetos, start=1):
        print(
            f"{indice}. Nome: {projeto.nome} | Área: {projeto.area} | "
            f"Faturamento: R$ {projeto.faturamento:,.2f}"
        )

    total = sum(p.faturamento for p in projetos)
    print(f"\nTotal de projetos: {len(projetos)} | Faturamento total: R$ {total:,.2f}")


def main() -> None:
    projetos = carregar_projetos()
    try:
        while True:
            opcao = exibir_menu()
            if opcao == '1':
                cadastrar_projeto(projetos)
            elif opcao == '2':
                listar_projetos(projetos)
            elif opcao == '3':
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário. Encerrando...")


if __name__ == "__main__":
    main()