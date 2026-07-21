import operator

def calculadora():
    """
    Uma calculadora que exemplifica o design desacoplado.
    O dicionário 'ops' atua como uma interface de despacho.
    """
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
    }

    print("--- Calculadora Python Modular ---")
    print("Operações: +, -, *, /, ^ (potência)")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        op = input("Digite o operador: ")
        num2 = float(input("Digite o segundo número: "))

        if op in ops:
            resultado = ops[op](num1, num2)
            print(f"Resultado: {num1} {op} {num2} = {resultado}")
        else:
            print("Erro: Operador inválido.")
            
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida na aritmética real.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números.")

if __name__ == "__main__":
    calculadora()