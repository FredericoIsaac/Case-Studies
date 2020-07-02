import turtle

def quadrado(lado):
    """
    Desenha um quadrado de lado = lado
    """
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    

if __name__ == "_main_":
    meu_lado = 50
    quadrado(meu_lado)