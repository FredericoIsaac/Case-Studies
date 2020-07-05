
# Algoritmo para descobrir o maior valor
def max_elem_1(elementos, funcao):
    """ Qual é o elemento de maior valor de acordo com a função. """
    
    # Inicializa
    melhor_valor = None
    melhor_elem = None

    # Testa e atualiza
    for elem in elementos:
        valor = funcao(elem)
        if melhor_valor == None or valor > melhor_valor:
            # Atualiza
            melhor_valor = valor
            melhor_elem = elem
    
    return melhor_elem

# Algoritmo para descobrir o maior valor (+ eficiente), tendo em conta que existe pelo menos um elemento
def max_elem_2(elementos, funcao):
    """ Qual é o elemento de maior valor de acordo com a função. """

    # Inicializa
    melhor_elem = elementos[0]
    melhor_valor = funcao(melhor_elem)

    # Testa e atualiza
    for elem in elementos[1:]:
        valor = funcao(elem)
        if valor > melhor_valor:
            # Atualiza
            melhor_valor = valor
            melhor_elem = elem

    return melhor_elem

# Algoritmo para descobrir o maior valor (Python way)
def max_elem_3(elementos, funcao):
    """ Qual é o elemento de maior valor de acordo com a função. """

    return max(elementos, key=funcao)