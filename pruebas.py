def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_hasta_n(n):
    primos = []
    for i in range(2, n + 1):
        if es_primo(i):
            primos.append(i)
    return primos

# Ejemplo de uso
if __name__ == "__main__":
    n = int(input("Introduce un número: "))
    print(f"Los números primos hasta {n} son: {primos_hasta_n(n)}")
