
# Objetivos:
    
## Geral

Percorrer o livro "Programação em Python" de ***Ernesto Costa***, tirar apontamentos, fazer exercicios com o visual studio, tudo em 30 dias.

[Livro: Programação em Python
Fundamentos e Resolução de Problemas](https://www.wook.pt/livro/programacao-em-python-ernesto-costa/17043335)

### Plano para cumprir objetivo

São 583 paginas, 583 / 30 dias =  19.43, por isso tenho que fazer uma média de 20 paginas por dia, para dia 31/07/2020 acabar o livro.


## 01/07/2020

Pagina atual: 3

Compilador: um programa que traduz a linguagem de programação para linguagem de maquina (binario?) e depois é que executa

Interpretador: executa diretamente as instruções.

>The main difference is that an interpreter directly executes the instructions in the source programming language while a compiler translates those instructions into efficient machine code.
An interpreter will typically generate an efficient intermediate representation and immediately evaluate it. 
[Source](https://medium.com/hackernoon/compilers-and-interpreters-3e354a2e41cf#:~:text=The%20main%20difference%20is%20that,representation%20and%20immediately%20evaluate%20it.)

### Tipos de Linguagens:

#### Linguagens declarativas ou relacionais:

    Algorithm = Logic + Control

>What is Logic Programming?
Logic programming is a programming strategy that uses logic circuits to control how facts and rules are expressed, rather than only mathematical functions. Often used in genetic and evolutionary programming, **this approach generally tells a model what goal to accomplish, rather than how to accomplish it.** Instead of a carefully structured control flow dictating when to execute and how to evaluate function calls or other instructions, the program’s logic rules are written as logical clauses (predicates). [Source](https://deepai.org/machine-learning-glossary-and-terms/logic-programming)

Por exemplo: Prolog

#### Linguagens Funcionais:

    Algorithm = Data + Functions

>Functional programming (often abbreviated FP) is the process of building software by **composing pure functions, avoiding shared state, mutable data, and side-effects.** Functional programming is declarative rather than imperative, and application state flows through pure functions.

(...)

>A **pure function** is a function which:
Given the same inputs, always returns the same output, and
Has no side-effects

(...)

>**Shared state** is any variable, object, or memory space that exists in a shared scope, or as the property of an object being passed between scopes. A shared scope can include global scope or closure scopes. Often, in object oriented programming, objects are shared between scopes by adding properties to other objects.

(...)

>An **immutable object** is an object that can’t be modified after it’s created. Conversely, a mutable object is any object which can be modified after it’s created.
Immutability is a central concept of functional programming because without it, the data flow in your program is lossy. State history is abandoned, and strange bugs can creep into your software. 

(...)

>A **side effect** is any application state change that is observable outside the called function other than its return value. Side effects include:
>* Modifying any external variable or object property (e.g., a global variable, or a variable in the parent function scope chain)
>* Logging to the console
>* Writing to the screen
>* Writing to a file
>* Writing to the network
>* Triggering any external process
>* Calling any other functions with side-effects

 [Source](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0#:~:text=Functional%20programming%20often%20abbreviated%20FP,state%20flows%20through%20pure%20functions.)

Por exemplo: Lisp

#### Linguagens Imperativas ou Procedimentais:

Um programa procedimental é caracterizado por uma sequência de instruções que atuam sobre os dados (variáveis), alterando de forma destrutiva o seu valor, ou sobre a ordem pela qual as instruções são executadas (instruções de controlo)

    Programa = Estrutura de Dados + Algoritmo

Por exemplo: C

#### Linguagens Orientadas aos Objetos (POO):

A comunicação com o exterior das funções é feita unicamente através dos parâmetros que lhe são passados. Divide o estado global por pequenas estruturas fechadas denominadas objetos.

O que distingue a POO da programação imperativa tradicional é o facto de um programa dever agora ser visto como um conjunto de objetos que são manipulados pelas operações às quais estão intimamente ligados.

    Orientação aos Objetos = Objetos + Classes + Herança
    POO = Orientação aos Objetos + Mensagens

Os objetos devem ser vistos como entidades que encapsulam não apenas dados, mas também operações sobre os dados.

**Herança** é um modo de definir a forma como as novas classes herdam propriedades das classes que lhes estão acima na hierarquia. As **mensagens** são o que permite a comunicação entre objetos. 

![exemplo-POO](/Python/images/whatis-object_oriented_programming_half_column_mobile.png)

Por exemplo: Java


Até pagina: 26

## 02/07/2020

Pagina atual: 27

## Modulos

Quando importamos um modulo temos que prefixar todos os comandos pelo nome do modulo.

    >>> import math
    >>> dir(math)
    ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
    >>> help(math.sin)
    Help on built-in function sin in module math:

    sin(x, /)
        Return the sine of x (measured in radians).

No terminal podemos "estudar" o modulo.

import math - para importar modulos

math.pi - para aceder ao pi no modulo math

dir(math) - inpeciona o que o modulo pode fazer apresentando uma lista no terminal com todos metodos 

help(math.sin) - diz nos o que o metodo faz


## Programa Tartaruga

    import turtle
    turtle.forward(x)
    turtle.left(x)
    turtle.right(x)
    turtle.backward(x)
    turtle.position()
    turtle.heading()
    turtle.goto(100,100)
    turtle.setx(200)
    turtle.ycor()
    turtle.xcor()
    turtle.setheading(225)
    turtle.hideturtle()
    turtle.showturtle()
    turtle.penup()
    turtle.pendown()
    turtle.shape("triangle")
    turtle.exitonclick() - permite controlar o fim da execução do programa através do fecho da janela usada para desenhar

Desenhar polígonos regulares:

    def poligono_regular(comp_lado, num_lados):
    ...     """
    ...     Desenha um polígono regular.
    ...     """
    ...     angulo_viragem = 360 / num_lados
    ...     for i in range(num_lados):
    ...         turtle.forward(comp_lado)
    ...         turtle.right(angulo_viragem)
    ...     turtle.hideturtle()


#### Contrutor

Permite criar um objeto. Se a operação não tiver argumento cria um objeto particular, se tiver argumento, tenta criar um objeto do tipo a partir do objeto fornecido.

[Source:](https://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/#:~:text=A%20constructor%20is%20a%20special,will%20need%20when%20it%20starts.)

>A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts. Constructors can also verify that there are enough resources for the object and perform any other start-up task you can think of.

>The name of a constructor is always the same, __init__(). The constructor can accept arguments when necessary to create the object. When you create a class without a constructor, Python automatically creates a default constructor for you that doesn’t do anything. Every class must have a constructor, even if it simply relies on the default constructor. 

[Source:](https://www.geeksforgeeks.org/constructors-in-python/)

Syntax of constructor declaration :

    class GeekforGeeks: 
    
        # default constructor 
        def __init__(self): 
            self.geek = "GeekforGeeks"
    
        # a method for printing data members 
        def print_Geek(self): 
            print(self.geek) 
    
    
    # creating object of the class 
    obj = GeekforGeeks() 
    
    # calling the instance method using the object obj 
    obj.print_Geek() 
_____
    Output :

    GeekforGeeks

#### Objeto
 
 Tres caracteristica são identidade, valor e tipo

 * Identidade - é o que torna o objeto unico, podendo ser consultado mas não modificado, é uma referência ou um pontador para uma zona da memória na qual se encontra a descrição do objeto
 * Valor - Traduz o estado do objeto num dado movimento.
 * Tipo - Determina o conjunto de valroes que o objeto pode assumir e as operações que com ele podemos fazer.

 Em Python o tipo é uma propriedade do objeto, podendo ser consultado mas não alterado, são implementados como classes.

![objetos](/Python\images\objetos.JPG)
 #### Classes

 É um modelo para descrever o que o conjunto dos objetos da classe partilham, em particular seus atributos, que definem o estado do objeto e as operações que com ele podem ser feitas, definidoras do seu comportamento.

#### Metodo: 

    objeto.método(argumentos)

Quando invocamos um metodo são executadas duas ações: primeiro, vai-se obter o método associado ao objeto através do seu nome; segundo, executa-se o método sobre o objeto, passando-lhe os argumentos, ou seja, fazemos:

    método(objeto, argumentos)

Quando usamos função é so este segundo passo.

#### Functions

Functions that can accept other functions as arguments are also called **higher-order functions**

Pagina atual: 63


## 03/07/2020




# Teste cohecimentos

## 1º Capitulo

Perguntas dadas no final do capitulo e as suas respotas

1. Quais as componentes de base da arquitetura de um computador?
    
R: São as seguintes: Dispositivo de entrada (rato/ teclado), CPU, Memória interna (RAM), Memória externa (disco rigido), Dispositivos de Saida (Monitor)

2. Compiladores e interpretadores: o que são e quais as diferenças entre eles?

R: Compiladores, é um programa que transforma a linguagem de programação como por exemplo c o clang, em linguagem máquina e depois é que executa. E um interpretadore executa diretamente a partir da source do programa

3. Que tipo de paradigmas de programação conhece? o que os distingue?

R: 
* Linguagem Declarativa ou relacionais - as linguagens declarativas têm uma natureza declarativa, significando isto que programar não envolve a indicação do modo como a solução se obtem mas apenas a definição do que é a solução.
* Linguagens Funcionais - é formado por um conjunto de funções relacionadas entre si.
* Linguagens Imperativas - Um programa procedimental é caracterizado por uma sequência de instruções que atuam sobre os dados (variáveis), alterando de forma destrutiva o seu valor, ou sobre a ordem pela qual as instruções são executadas (instruções de controlo)
* Linguagem Orientadas aos objetos - o facto de um programa dever agora ser visto como um conjunto de objetos que são manipulados pelas operações às quais estão intimamente ligados.

4. O que são módulos, expressões, instruções e objetos?

[Site com os conceitos](https://panda.ime.usp.br/pensepy/static/pensepy/02-Conceitos/conceitos.html)

R: 
* Modulos são ficheiros com código que permitem aumentar as capacidades da linguagem de base.
* Expressões é uma combinação de valores, variáveis, operadores e chamadas de funções
* Instruções que o interpretador pode executar
* Objetos, também conhecido como valor. Objetos são elementos fundamentais. Programas são projetados para manipular esses elementos (ou programadores dão ordens para que operações sejam realizadas sobre eles).

5. O que entende por parâmetros formais?

[Site com os conceitos](http://excript.com/python/parametro-de-funcao-python.html)

R: Parâmetro é uma variável declarada no cabeçalho da função e tem uso exclusivo dentro do bloco de instrução da mesma.

6. O que faz a instrução de atribuição (=)

R: Atribui a variavel do lado direito (objeto) o valor do lado direito

7. Que instruções de controlo conhece e para que servem?

R:
* Instruções de atribuição - da ao objeto um valor
* Instruções de controlo - if-then-else, sao instruções que nao alteram o estado dos objetos e se limitam a indicar a parte que deve ser executada

8. O que entende pelo modelo PCAP?

R: Primitivas, Composição, Abstração e Padrões.
* Primitivas - + * < =  (numeros, cadeias, caracteres)
* Composição - if for (Listas, dicionários, conjuntos)
* Abstração - def (classes)
* Padrões - Funções de segunda ordem (funções genericas)

9. O que entende por ciclo lê - avalia - escreve?

[Site com os conceitos](https://www.freecodecamp.org/news/this-is-why-your-read-eval-print-loop-is-so-amazing-cf0362003983/)

[Site com os conceitos](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)

R: Interactive computer programming environment that takes (read) single user inputs (i.e., single expressions), evaluates (executes/ write) them, and returns the result to the user and then go back to the start to read your next input.

## 2º Capitulo

1. O que entende por construtor?

R: It instantiates an object using the definitions found in your class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts.

2. Quais são as operações básicas sobre tartarugas?

R: 

    turtle.forward(x)
    turtle.left(x)
    turtle.right(x)
    turtle.backward(x)

3. De que modo se definem novas formas de tartaruga?

R: turtle.shape("triangle")

4. Quais são as operações básicas sobre caneta?

R:
* turtle.penup()
* turtle.pendown()

5. O que distingue uma função de um método?

R: Num método primeiro, vai-se obter o método associado ao objeto através do seu nome; segundo, executa-se o método sobre o objeto, passando-lhe os argumentos. Numa função so se faz o segundo passo.

6. Como podemos controlar a escala do nosso desenho?

R: setworldcoordinates ( canto inferior esquerdo, canto inferior esquerdo, canto superior direiro, canto superior direiro)

    setworldcoordinates(-math.pi, -2 , math.pi, 2)

7. Qual é a finalidade de exitonclick()?

R: Permite controlar o fim da execução do programa através do fecho da janela usada para desenhar

8. Porque podemos usar funções como argumentos de funções e que consequências existem desse facto?

R: Podemos usar porque em python tudo são objetos, inclusive funções. Functions that can accept other functions as arguments are also called higher-order functions




# Python Sintax

    >>> altura = eval(input("altura:"))
    altura:1.81
    >>> peso = (72.7 * altura) - 58
    >>> print(peso)
    73.58700000000002

print() - imprime e default é aseguir quebra a linha

input() - solicita a introdução de dados

eval() - permite interpretar o dado introduzido (se nao colocarmos o valor introduzido tera o tipo de string, neste exemplo senao coloca se iria dar erro pois seria um float * string)

for i in range(5): - vai repetir de 0 a 4

import math - para importar modulos

math.pi - para aceder ao pi no modulo math

dir(math) - inpeciona o que o modulo pode fazer apresentando uma lista no terminal com todos metodos 

help(math.sin) - diz nos o que o metodo faz

random.randint(0,100) - numero aleatorio de 0 a 100 (import random)

    >>> 1.0/2
    0.5
    >>> 1.0//2
    0.0

1.0 // 2 - ao usar // dois seguidos vai fazer a divisão e como numero inteiro

