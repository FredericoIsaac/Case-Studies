
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