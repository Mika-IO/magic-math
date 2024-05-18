import math

def calcular_raiz_quadrada(num):
    return math.sqrt(num)

def calcular_exponenciacao(base, exp):
    return math.pow(base, exp)

def calcular_logaritmos(value):
    log_natural = math.log(value)
    log_base10 = math.log10(value)
    return log_natural, log_base10

def calcular_funcoes_trigonometricas(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    tangente = math.tan(angulo_radianos)
    return seno, cosseno, tangente

def calcular_funcoes_hiperbolicas(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    seno_hiperbolico = math.sinh(angulo_radianos)
    cosseno_hiperbolico = math.cosh(angulo_radianos)
    tangente_hiperbolica = math.tanh(angulo_radianos)
    return seno_hiperbolico, cosseno_hiperbolico, tangente_hiperbolica

def mostrar_constantes_matematicas():
    return math.pi, math.e

def main():
    num = 16
    print(f"A raiz quadrada de {num} é {calcular_raiz_quadrada(num)}")

    base = 2
    exp = 3
    print(f"{base} elevado a {exp} é {calcular_exponenciacao(base, exp)}")

    value = 10
    log_natural, log_base10 = calcular_logaritmos(value)
    print(f"O logaritmo natural de {value} é {log_natural}")
    print(f"O logaritmo na base 10 de {value} é {log_base10}")

    angulo_graus = 45
    seno, cosseno, tangente = calcular_funcoes_trigonometricas(angulo_graus)
    print(f"Seno de {angulo_graus} graus é {seno}")
    print(f"Cosseno de {angulo_graus} graus é {cosseno}")
    print(f"Tangente de {angulo_graus} graus é {tangente}")

    seno_hiperbolico, cosseno_hiperbolico, tangente_hiperbolica = calcular_funcoes_hiperbolicas(angulo_graus)
    print(f"Seno hiperbólico de {angulo_graus} graus é {seno_hiperbolico}")
    print(f"Cosseno hiperbólico de {angulo_graus} graus é {cosseno_hiperbolico}")
    print(f"Tangente hiperbólica de {angulo_graus} graus é {tangente_hiperbolica}")

    pi, e = mostrar_constantes_matematicas()
    print(f"O valor de pi é {pi}")
    print(f"O valor de e é {e}")

if __name__ == "__main__":
    main()
