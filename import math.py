import math


def eh_quadrado_perfeito(n):
    if n < 0:
        return False

    raiz = math.isqrt(n)
    return raiz * raiz == n


def solicitar_inteiro(prompt, minimo=None):
    while True:
        valor_texto = input(prompt).strip()
        try:
            valor = int(valor_texto)
            if minimo is not None and valor < minimo:
                print(f"Valor inválido. Digite um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main():
    print("=== Verificador de Quadrado Perfeito ===")
    numero = solicitar_inteiro("Digite um número inteiro para verificar: ")

    if eh_quadrado_perfeito(numero):
        print(f"O número {numero} é um quadrado perfeito!")
    else:
        print(f"O número {numero} não é um quadrado perfeito.")


if __name__ == "__main__":
    main()