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

