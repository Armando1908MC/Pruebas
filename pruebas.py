def criba_eratostenes(n):
    """
    Implementa la Criba de Eratóstenes para encontrar todos los números primos hasta n.
    :param n: Límite superior.
    :return: Lista de números primos.
    """
    if n < 2:
        return []

    # Crear una lista para marcar números compuestos
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            # Marcar múltiplos de i como no primos
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    # Filtrar los índices que son primos
    return [i for i, primo in enumerate(es_primo) if primo]

def primos_y_factorizacion(n):
    """
    Encuentra los primos hasta n y genera la factorización de un número dado.
    :param n: Límite superior para los primos.
    :return: Lista de números primos.
    """
    primos = criba_eratostenes(n)
    print(f"Primos hasta {n}: {primos}")

    # Factorización de números
    def factoriza(num):
        factores = []
        for p in primos:
            while num % p == 0:
                factores.append(p)
                num //= p
            if num == 1:
                break
        if num > 1:
            factores.append(num)  # Si queda un factor mayor que sqrt(n)
        return factores

    # Ejemplo de factorización
    print("\nFactorización de números:")
    for i in range(2, n + 1):
        print(f"{i}: {factoriza(i)}")

if __name__ == "__main__":
    numero = int(input("Introduce un número límite: "))
    primos_y_factorizacion(numero)
