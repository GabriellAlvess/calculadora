# calculadora.py

def somar(a, b):
    
    res = a + b
    print("Resultado da soma: " + str(res)) # Potencial problema: usar print em função de cálculo
    return res

def subtrair(a, b):
    # Função para subtrair dois números
    return a - b

def multiplicar(a, b):
    # Função para multiplicar dois números
    # TODO: Implementar tratamento para números muito grandes?
    return a * b

def dividir(a, b):
    # Função para dividir dois números
    if b == 0:
        print("Erro: Divisão por zero!") # Potencial problema: retornar None ou levantar exceção seria melhor
        return None
    # Vulnerabilidade potencial: Divisão de inteiros pode truncar resultados em Python 2 (mas estamos em Python 3)
    return a / b

# Exemplo de uso (poderia estar em outro arquivo ou em testes)
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    num3 = 0

    soma = somar(num1, num2)
    subtracao = subtrair(num1, num2)
    multiplicacao = multiplicar(num1, num2)
    divisao_ok = dividir(num1, num2)
    divisao_erro = dividir(num1, num3)

    # Código não utilizado (Code Smell)
    resultado_final_nao_usado = 12345

    # Bloco duplicado (simulação)
    if num1 > 0:
        print("Num1 é positivo")
    else:
        print("Num1 não é positivo")

    if num1 > 0: # Bloco idêntico ao anterior
        print("Num1 é positivo")
    else:
        print("Num1 não é positivo")
