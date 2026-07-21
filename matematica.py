import sympy # Biblioteca poderosa para matemática teórica
import matplotlib.pyplot as plt

# Vamos contar quantos números primos existem até cada número N
def contar_primos(n_max):
    contagem = []
    for i in range(1, n_max + 1):
        # A função isprime retorna True se for primo
        if sympy.isprime(i):
            contagem.append(1)
        else:
            contagem.append(0)
    
    # Fazemos a soma acumulada para ver a curva de crescimento
    import itertools
    return list(itertools.accumulate(contagem))

N = 1000
dados = contar_primos(N)

plt.plot(dados)
plt.title("Distribuição dos Números Primos (Padrão de Crescimento)")
plt.xlabel("N (Números Inteiros)")
plt.ylabel("Quantidade de Primos")
plt.show()